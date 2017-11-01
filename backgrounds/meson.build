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
  'adwaita-lock.jpg',
  'adwaita-morning.jpg',
  'adwaita-night.jpg',
  'Bokeh_Tails.jpg',
  'Chmiri.jpg',
  'Dark_Ivy.jpg',
  'Fabric.jpg',
  'Flowerbed.jpg',
  'Godafoss_Iceland.jpg',
  'Icescape.jpg',
  'Mirror.jpg',
  'Road.jpg',
  'Sandstone.jpg',
  'Signpost_of_the_Shadows.jpg',
  'Stones.jpg',
  'symbolics-1.png',
  'symbolics-2.jpg',
  'Terraform-green.jpg',
  'Waterfalls.jpg',
  'Waves.jpg'
]

install_data([adwaita_timed] + backgrounds, install_dir: backgrounddir)

foreach metadata : ['gnome-backgrounds.xml', 'adwaita.xml']
  i18n.merge_file(metadata,
    input: configure_file(
      input: metadata + '.in.in',
      output: metadata + '.in',
      configuration: dataconf
    ),
    output: metadata,
    po_dir: '../po',
    data_dirs: '..',
    install: true,
    install_dir: metadatadir
  )
endforeach
