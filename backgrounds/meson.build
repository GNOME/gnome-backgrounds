dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'adwaita-d.webp',
  'adwaita-l.webp',
  'blobs-d.svg',
  'blobs-l.svg',
  'design-is-rounded-rectangles-d.webp',
  'design-is-rounded-rectangles-l.webp',
  'drool-d.svg',
  'drool-l.svg',
  'dune-d.svg',
  'dune-l.svg',
  'fold-d.webp',
  'fold-l.webp',
  'keys-d.webp',
  'keys-l.webp',
  'oceans.svg',
  'pills-d.webp',
  'pills-l.webp',
  'pixels-d.webp',
  'pixels-l.webp',
  'symbolic-d.webp',
  'symbolic-l.webp',
  'truchet-d.webp',
  'truchet-l.webp',
  'vnc-d.webp',
  'vnc-l.webp'
]

install_data(backgrounds, install_dir: backgrounddir)

foreach metadata : [
  'adwaita.xml',
  'blobs.xml',
  'drool.xml',
  'design-is-rounded-rectangles.xml', 
  'dune.xml',
  'fold.xml',
  'keys.xml',
  'oceans.xml',
  'pills.xml',
  'pixels.xml',
  'symbolic.xml',
  'truchet.xml',
  'vnc.xml']
  configure_file(
    input: metadata + '.in',
    output: metadata,
    configuration: dataconf,
    install: true,
    install_dir: metadatadir
  )
endforeach
