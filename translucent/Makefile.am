backgrounddir = $(datadir)/pixmaps/backgrounds/gnome/translucent

background_DATA =\
	ellipsis.png \
	grid.png \
	masle.png \
	rects.png \
	tentacles.png \
	waves.png

metadata_in_files = gnome-translucent.xml.in
metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = $(metadata_in_files:.xml.in=.xml)
@INTLTOOL_XML_RULE@

noinst_DATA = gnome-translucent.xml.in
CLEANFILES = gnome-translucent.xml gnome-translucent.xml.in

EXTRA_DIST = $(background_DATA)

gnome-translucent.xml.in: gnome-translucent.xml.in.in Makefile
	sed -e 's^\@datadir\@^$(datadir)^g' < gnome-translucent.xml.in.in > gnome-translucent.xml.in.tmp \
	&& mv gnome-translucent.xml.in.tmp gnome-translucent.xml.in
