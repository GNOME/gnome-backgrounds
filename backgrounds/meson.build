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
  'candy-reborn-d.jxl',
  'candy-reborn-l.jxl',
  'curvy-d.jxl',
  'curvy-l.jxl',
  'drool-d.svg',
  'drool-l.svg',
  'fold-d.jxl',
  'fold-l.jxl',
  'geometrics-d.jxl',
  'geometrics-l.jxl',
  'glass-chip-d.jxl',
  'glass-chip-l.jxl',
  'lcd-rainbow-d.jxl',
  'lcd-rainbow-l.jxl',
  'map-d.svg',
  'map-l.svg',
  'morphogenesis-d.svg',
  'morphogenesis-l.svg',
  'neogeo-d.jxl',
  'neogeo-l.jxl',
  'pills-d.jxl',
  'pills-l.jxl',
  'pixel-pusher-d.jxl',
  'pixel-pusher-l.jxl',
  'pixels-d.jxl',
  'pixels-l.jxl',
  'sheet-d.jxl',
  'sheet-l.jxl',
  'symbolic-d.png',
  'symbolic-l.png',
  'swoosh-d.jxl',
  'swoosh-l.jxl',
  'tarka-d.jxl',
  'tarka-l.jxl',
  'tarkov-pills-d.jxl',
  'tarkov-pills-l.jxl',
  'vnc-d.png',
  'vnc-l.png'
]

install_data(backgrounds, install_dir: backgrounddir)

foreach metadata : [
  'adwaita.xml',
  'amber.xml',
  'blobs.xml',
  'candy-reborn.xml',
  'curvy.xml',
  'drool.xml',
  'fold.xml',
  'geometrics.xml',
  'glass-chip.xml',
  'lcd-rainbow.xml',
  'map.xml',
  'morphogenesis.xml',
  'neogeo.xml',
  'pills.xml',
  'pixel-pusher.xml',
  'pixels.xml',
  'sheet.xml',
  'symbolic.xml',
  'swoosh.xml',
  'tarka.xml',
  'tarkov-pills.xml',
  'vnc.xml']
  configure_file(
    input: metadata + '.in',
    output: metadata,
    configuration: dataconf,
    install: true,
    install_dir: metadatadir
  )
endforeach
