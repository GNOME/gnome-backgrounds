dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'adwaita-d.jpg',
  'adwaita-l.jpg',
  'amber-d.jxl',
  'amber-l.jxl',
  'blobs-d.svg',
  'blobs-l.svg',
  'design-is-rounded-rectangles-d.jpg',
  'design-is-rounded-rectangles-l.jpg',
  'drool-d.svg',
  'drool-l.svg',
  'fold-d.jpg',
  'fold-l.jpg',
  'geometrics-d.jxl',
  'geometrics-l.jxl',
  'geometrics2-d.jxl',
  'geometrics2-l.jxl',
  'geometrics3-d.jxl',
  'geometrics3-l.jxl',
  'geometrics3-d.jxl',
  'geometrics3-l.jxl',
  'keys-d.jpg',
  'keys-l.jpg',
  'morphogenesis-d.svg',
  'morphogenesis-l.svg',
  'neogeo-d.jxl',
  'neogeo-l.jxl',
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
  'geometrics.xml',
  'geometrics2.xml',
  'geometrics3.xml',
  'geometrics4.xml',
  'keys.xml',
  'morphogenesis.xml',
  'neogeo.xml',
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
