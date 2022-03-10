dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'adwaita-d.jpg',
  'adwaita-l.jpg',
  'blobs-d.svg',
  'blobs-l.svg',
  'brush-strokes-d.jpg',
  'brush-strokes-l.jpg',
  'disco-d.jpg',
  'disco-l.jpg',
  'drool-d.svg',
  'drool-l.svg',
  'libadwaita-d.jpg',
  'libadwaita-l.jpg',  
  'pixels-d.png',
  'pixels-l.png',
  'symbolics-d.png',
  'symbolics-l.png',
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
  'brush-strokes.xml',
  'disco.xml',
  'drool.xml',
  'libadwaita.xml',
  'pixels.xml',
  'symbolics.xml',
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
