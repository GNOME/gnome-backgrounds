dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'adwaita-d.jxl',
  'adwaita-l.jxl',
  'blobs-d.svg',
  'blobs-l.svg',
  'drool-d.svg',
  'drool-l.svg',
  'dune-d.svg',
  'dune-l.svg',
  'field-d.svg',
  'field-l.svg',
  'grid-d.jpg',
  'grid-l.jpg',
  'licorice-d.jpg',
  'licorice-l.jpg',
  'pixels-d.png',
  'pixels-l.png',
  'symbolic-d.webp',
  'symbolic-l.webp',
  'truchet-d.jpg',
  'truchet-l.jpg',
  'vnc-d.png',
  'vnc-l.png',
  'wood-d.jpg',
  'wood-l.jpg'
]

install_data(backgrounds, install_dir: backgrounddir)

foreach metadata : [
  'adwaita.xml',
  'blobs.xml',
  'drool.xml',
  'dune.xml',
  'field.xml',
  'grid.xml',
  'licorice.xml',
  'pixels.xml',
  'symbolic.xml',
  'truchet.xml',
  'vnc.xml',
  'wood.xml']
  configure_file(
    input: metadata + '.in',
    output: metadata,
    configuration: dataconf,
    install: true,
    install_dir: metadatadir
  )
endforeach
