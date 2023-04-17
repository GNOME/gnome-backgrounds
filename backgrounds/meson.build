dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'adwaita-d.jpg',
  'adwaita-l.jpg',
  'blobs-d.svg',
  'blobs-l.svg',
  'design-is-rounded-rectangles-d.webp',
  'design-is-rounded-rectangles-l.webp',
  'drool-d.svg',
  'drool-l.svg',
  'fold-d.webp',
  'fold-l.webp',
  'keys-d.webp',
  'keys-l.webp',
  'oceans.svg',
  'pills-d.webp',
  'pills-l.webp',
  'pipes-d.jpg',
  'pipes-l.jpg',
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
  'fold.xml',
  'keys.xml',
  'oceans.xml',
  'pills.xml',
  'pipes.xml',
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
