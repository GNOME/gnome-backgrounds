dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

adwaita_timed = configure_file(
  input: 'adwaita-timed.xml.in',
  output: 'adwaita-timed.xml',
  configuration: dataconf
)

backgrounds = [
  'adwaita-d.png',
  'adwaita-l.png',
  'archi-d.jpg',
  'archi-l.jpg',
  'blobs-d.svg',
  'blobs-l.svg',
  'brush-strokes-d.jpg',
  'brush-strokes-l.jpg',
  'disco-d.jpg',
  'disco-l.jpg',
  'drool-d.svg',
  'drool-l.svg',
  'frosty-d.jpg',
  'frosty-l.jpg',
  'pixels-d.png',
  'pixels-l.png',
  'symbolics-d.png',
  'symbolics-l.png',
  'VNC.png',
  'wood-d.jpg',
  'wood-l.jpg'
]

install_data([adwaita_timed] + backgrounds, install_dir: backgrounddir)

foreach metadata : ['gnome-backgrounds.xml', 'adwaita.xml']
  configure_file(
    input: metadata + '.in',
    output: metadata,
    configuration: dataconf,
    install: true,
    install_dir: metadatadir
  )
endforeach
