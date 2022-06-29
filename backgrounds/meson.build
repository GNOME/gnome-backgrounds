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
  'grid-d.jxl',
  'grid-l.jxl',
  'licorice-d.jxl',
  'licorice-l.jxl',
  'oceans.svg',
  'pixels-d.jxl',
  'pixels-l.jxl',
  'symbolic-d.jxl',
  'symbolic-l.jxl',
  'truchet-d.jxl',
  'truchet-l.jxl',
  'vnc-d.jxl',
  'vnc-l.jxl',
  'wood-d.jxl',
  'wood-l.jxl'
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
