project('gnome-backgrounds',
  version: '40.rc',
  meson_version: '>= 0.41.0'
)

i18n = import('i18n')

prefix = get_option('prefix')

datadir = join_paths(prefix, get_option('datadir'))
backgrounddir = join_paths(datadir, 'backgrounds', 'gnome')
metadatadir = join_paths(datadir, 'gnome-background-properties')

subdir('backgrounds')
