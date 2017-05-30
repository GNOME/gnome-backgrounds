project('gnome-backgrounds', 'c',
  version: '3.22.1',
  meson_version: '0.41.0'
)

i18n = import('i18n')

prefix = get_option('prefix')

datadir = join_paths(prefix, get_option('datadir'))
backgrounddir = join_paths(datadir, 'background', 'gnome')
metadatadir = join_paths(datadir, 'gnome-background-properties')

subdir('backgrounds')
subdir('po')
