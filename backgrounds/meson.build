dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'adwaita-d.webp',
  'adwaita-l.webp',
  'blobs-d.svg',
  'blobs-l.svg',
  'drool-d.svg',
  'drool-l.svg',
  'dune-d.svg',
  'dune-l.svg',
  'field-d.svg',
  'field-l.svg',
  'grid-d.webp',
  'grid-l.webp',
  'licorice-d.webp',
  'licorice-l.webp',
  'oceans.svg',
  'pixels-d.webp',
  'pixels-l.webp',
  'symbolic-d.webp',
  'symbolic-l.webp',
  'truchet-d.webp',
  'truchet-l.webp',
  'vnc-d.webp',
  'vnc-l.webp',
  'wood-d.webp',
  'wood-l.webp'
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
  'oceans.xml',
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
