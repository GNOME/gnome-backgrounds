backgrounddir = $(datadir)/pixmaps/backgrounds/gnome/tiles

background_DATA =\
	alien-artifact-trans.png \
	tiles-trans.png \
	cow-trans.png \
	greche.png \
	leather_skin-resynth-hig.png \
	stone-wall.png


metadata_in_files = gnome-tiles.xml.in
metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = $(metadata_in_files:.xml.in=.xml)
@INTLTOOL_XML_RULE@

noinst_DATA = gnome-tiles.xml.in
CLEANFILES = gnome-tiles.xml gnome-tiles.xml.in

EXTRA_DIST = $(background_DATA)

gnome-tiles.xml.in: gnome-tiles.xml.in.in Makefile
	sed -e 's^\@datadir\@^$(datadir)^g' < gnome-tiles.xml.in.in > gnome-tiles.xml.in.tmp \
	&& mv gnome-tiles.xml.in.tmp gnome-tiles.xml.in

MAINTAINERCLEANFILES = \
	Makefile.in
