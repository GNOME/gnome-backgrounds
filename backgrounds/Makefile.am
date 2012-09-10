backgrounddir = $(datadir)/backgrounds/gnome

background_DATA =\
	Blinds.jpg \
	BlueMarbleWest.jpg \
	Chmiri.jpg \
	Fabric.jpg \
	FootFall.png \
	Mirror.jpg \
	Road.jpg \
	Sandstone.jpg \
	Spaceflare.jpg \
	Stripes.jpg \
	Stripes34.jpg \
	Sunset.jpg \
	Terraform-green.jpg \
	Tulip.jpg \
	UnderLit.jpg \
	Wood.jpg \
	Waves.jpg \
	ZvonecKonec.jpg

metadata_in_files = gnome-backgrounds.xml.in
metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = $(metadata_in_files:.xml.in=.xml)
@INTLTOOL_XML_RULE@

noinst_DATA = gnome-backgrounds.xml.in
CLEANFILES = gnome-backgrounds.xml gnome-backgrounds.xml.in

EXTRA_DIST = $(background_DATA) gnome-backgrounds.xml.in.in

edit = sed \
	-e 's|@BACKGROUNDDIR[@]|$(backgrounddir)|g'

gnome-backgrounds.xml.in: gnome-backgrounds.xml.in.in Makefile
	$(edit) $< >$@

MAINTAINERCLEANFILES = \
	Makefile.in

-include $(top_srcdir)/git.mk
