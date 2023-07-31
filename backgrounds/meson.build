dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'adwaita-d.jxl',
  'adwaita-l.jxl',
  'blobs-d.svg',
  'blobs-l.svg',
  'design-is-rounded-rectangles-d.jxl',
  'design-is-rounded-rectangles-l.jxl',
  'drool-d.svg',
  'drool-l.svg',
  'fold-d.jxl',
  'fold-l.jxl',
  'keys-d.jxl',
  'keys-l.jxl',
  'morphogenesis-d.svg',
  'morphogenesis-l.svg',
  'pills-d.jxl',
  'pills-l.jxl',
  'pipes-d.jxl',
  'pipes-l.jxl',
  'pixels-d.jxl',
  'pixels-l.jxl',
  'symbolic-d.jxl',
  'symbolic-l.jxl',
  'truchet-d.jxl',
  'truchet-l.jxl',
  'vnc-d.jxl',
  'vnc-l.jxl'
]

install_data(backgrounds, install_dir: backgrounddir)

foreach metadata : [
  'adwaita.xml',
  'blobs.xml',
  'drool.xml',
  'design-is-rounded-rectangles.xml', 
  'fold.xml',
  'keys.xml',
  'morphogenesis.xml',
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
