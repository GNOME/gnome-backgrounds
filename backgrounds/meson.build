dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'adwaita-d.jxl',
  'adwaita-l.jxl',
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
  'lcd-blue-d.jxl',
  'lcd-blue-l.jxl',
  'lcd-green-d.jxl',
  'lcd-green-l.jxl',
  'legacy-d.jxl',
  'legacy-l.jxl',
  'mollnar-d.svg',
  'mollnar-l.svg',
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
  'sheet-d.jxl',
  'sheet-l.jxl',
  'symbolic-d.png',
  'symbolic-l.png',
  'symbolic-soup-d.jxl',
  'symbolic-soup-l.jxl',
  'swoosh-d.jxl',
  'swoosh-l.jxl',
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
  'lcd-blue.xml',
  'lcd-green.xml',
  'legacy.xml',
  'mollnar.xml',
  'morphogenesis.xml',
  'neogeo.xml',
  'pills.xml',
  'pixels.xml',
  'ring.xml',
  'sheet.xml',
  'symbolic.xml',
  'symbolic-soup.xml',
  'swoosh.xml',
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
