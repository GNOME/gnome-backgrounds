backgrounddir = $(datadir)/pixmaps/backgrounds/gnome/nature

background_DATA =\
	Aqua.jpg \
	Blinds.jpg \
	Dune.jpg \
	FreshFlower.jpg \
	Garden.jpg \
	GreenMeadow.jpg \
	LadyBird.jpg \
	RainDrops.jpg \
	Storm.jpg \
	TwoWings.jpg \
	Wood.jpg \
	YellowFlower.jpg

metadata_in_files = gnome-nature.xml.in
metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = $(metadata_in_files:.xml.in=.xml)
@INTLTOOL_XML_RULE@

noinst_DATA = gnome-nature.xml.in
CLEANFILES = gnome-nature.xml gnome-nature.xml.in

EXTRA_DIST = $(background_DATA) gnome-nature.xml.in.in

gnome-nature.xml.in: gnome-nature.xml.in.in Makefile
	sed -e 's^\@datadir\@^$(datadir)^g' < $(srcdir)/gnome-nature.xml.in.in > gnome-nature.xml.in.tmp \
	&& mv gnome-nature.xml.in.tmp gnome-nature.xml.in

MAINTAINERCLEANFILES = \
	Makefile.in
