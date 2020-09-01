dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

adwaita_timed = configure_file(
  input: 'adwaita-timed.xml.in',
  output: 'adwaita-timed.xml',
  configuration: dataconf
)

backgrounds = [
  'adwaita-day.jpg',
  'adwaita-morning.jpg',
  'adwaita-night.jpg',
  'Acrylic.jpg',
  'ColdWarm.jpg',
  'Dark_Ivy.jpg',
  'Endless-shapes.jpg',
  'LightWaves.jpg',
  'Icetwigs.jpg',
  'Road.jpg',
  'Stripes.jpg',
  'SeaSunset.jpg',
  'Symbolics-1.jpg',
  'Symbolics-2.jpg',
  'VNC.png',
  'Wood.jpg'
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
