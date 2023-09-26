dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'adwaita-d.jpg',
  'adwaita-l.jpg',
  'amber-d.jpg',
  'amber-l.jpg',
  'blobs-d.svg',
  'blobs-l.svg',
  'design-is-rounded-rectangles-d.jpg',
  'design-is-rounded-rectangles-l.jpg',
  'drool-d.svg',
  'drool-l.svg',
  'fold-d.jpg',
  'fold-l.jpg',
  'keys-d.jpg',
  'keys-l.jpg',
  'morphogenesis-d.svg',
  'morphogenesis-l.svg',
  'pills-d.jpg',
  'pills-l.jpg',
  'pixels-d.jpg',
  'pixels-l.jpg',
  'stripes-d.jxl',
  'stripes-l.jxl',
  'symbolic-d.png',
  'symbolic-l.png',
  'tarka-d.jxl',
  'tarka-l.jxl',
  'vnc-d.png',
  'vnc-l.png'
]

install_data(backgrounds, install_dir: backgrounddir)

foreach metadata : [
  'adwaita.xml',
  'amber.xml',
  'blobs.xml',
  'drool.xml',
  'design-is-rounded-rectangles.xml', 
  'fold.xml',
  'keys.xml',
  'morphogenesis.xml',
  'pills.xml',
  'pixels.xml',
  'stripes.xml',
  'symbolic.xml',
  'tarka.xml',
  'vnc.xml']
  configure_file(
    input: metadata + '.in',
    output: metadata,
    configuration: dataconf,
    install: true,
    install_dir: metadatadir
  )
endforeach
