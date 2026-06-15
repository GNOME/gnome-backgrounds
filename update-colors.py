#!/usr/bin/env python3
"""Extract dominant colors from light-variant wallpapers and update XML metadata.

Uses k-means clustering on sampled pixels to pick pcolor (most dominant)
and scolor (second most dominant) for each wallpaper.
"""

import os
import re
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image
from sklearn.cluster import MiniBatchKMeans

sys.path.insert(0, '/tmp/gnome-bg-env/lib/python3.14/site-packages')
import pillow_jxl  # noqa: F401 - register JXL plugin

BACKGROUNDS_DIR = os.path.join(os.path.dirname(__file__), 'backgrounds')


def rgb_to_hex(rgb):
    return '#{:02X}{:02X}{:02X}'.format(*rgb)


def load_image(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == '.svg':
        result = subprocess.run(
            ['rsvg-convert', '--width', '1024', '--height', '1024', path],
            capture_output=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f'rsvg-convert failed: {result.stderr.decode()}')
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            f.write(result.stdout)
            tmp = f.name
        try:
            im = Image.open(tmp).convert('RGB')
        finally:
            os.unlink(tmp)
    else:
        im = Image.open(path).convert('RGB')
    return im


def extract_colors(image, n_colors=5, sample_ratio=0.02):
    arr = np.asarray(image)
    pixels = arr.reshape(-1, 3)

    unique = np.unique(pixels, axis=0)
    if len(unique) == 1:
        return [tuple(unique[0])]

    sample_size = max(1000, int(pixels.shape[0] * sample_ratio))
    if sample_size < pixels.shape[0]:
        idx = np.random.RandomState(0).choice(pixels.shape[0], sample_size, replace=False)
        pixels = pixels[idx]

    pixels = pixels.astype(np.float32)
    kmeans = MiniBatchKMeans(n_clusters=min(n_colors, len(unique)), random_state=0, batch_size=4096)
    kmeans.fit(pixels)

    labels = kmeans.labels_
    counts = np.bincount(labels)
    order = np.argsort(counts)[::-1]

    colors = [tuple(kmeans.cluster_centers_[i].astype(int)) for i in order]
    return colors


def update_xml(xml_path, pcolor, scolor):
    with open(xml_path, 'rb') as f:
        raw = f.read()

    # Detect original line endings
    crlf = b'\r\n' in raw
    # Normalize to LF
    content = raw.replace(b'\r\n', b'\n').decode('utf-8')

    def replace_color(match):
        tag = match.group(1)
        return f'<{tag}>{pcolor if tag == 'pcolor' else scolor}</{tag}>'

    new_content = re.sub(
        r'<(pcolor|scolor)>#[A-Fa-f0-9]{6}</\1>',
        replace_color,
        content,
    )
    out = new_content.encode('utf-8')
    if crlf:
        out = out.replace(b'\n', b'\r\n')
    with open(xml_path, 'wb') as f:
        f.write(out)


def main():
    for fname in sorted(os.listdir(BACKGROUNDS_DIR)):
        if not re.search(r'-l\.(jpg|png|jxl|svg)$', fname):
            continue
        base = fname.rsplit('-l.', 1)[0]
        light_path = os.path.join(BACKGROUNDS_DIR, fname)
        xml_path = os.path.join(BACKGROUNDS_DIR, f'{base}.xml.in')

        if not os.path.exists(xml_path):
            print(f'SKIP {fname}: no matching XML')
            continue

        print(f'\n{base}:')
        print(f'  Loading {fname}...')
        try:
            im = load_image(light_path)
        except Exception as e:
            print(f'  ERROR loading: {e}')
            continue

        im.thumbnail((800, 800), Image.LANCZOS)
        colors = extract_colors(im, n_colors=5)
        hex_colors = [rgb_to_hex(c) for c in colors]
        print(f'  Dominant colors: {hex_colors}')

        pcolor = hex_colors[0]
        if len(hex_colors) >= 2:
            scolor = hex_colors[1]
        else:
            scolor = '#000000'

        update_xml(xml_path, pcolor, scolor)
        print(f'  -> pcolor={pcolor} scolor={scolor}')


if __name__ == '__main__':
    main()
