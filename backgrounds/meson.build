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
  'drool-d.svg',
  'drool-l.svg',
  'fold-d.jxl',
  'fold-l.jxl',
  'geometrics-d.jxl',
  'geometrics-l.jxl',
  'glass-chip-d.jxl',
  'glass-chip-l.jxl',
  'morphogenesis-d.svg',
  'morphogenesis-l.svg',
  'neogeo-d.jxl',
  'neogeo-l.jxl',
  'pills-d.jxl',
  'pills-l.jxl',
  'pixels-d.jpg',
  'pixels-l.jpg',
  'ring-d.jxl',
  'ring-l.jxl',
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
  'fold.xml',
  'geometrics.xml',
  'glass-chip.xml',
  'morphogenesis.xml',
  'neogeo.xml',
  'pills.xml',
  'pixels.xml',
  'ring.xml',
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
