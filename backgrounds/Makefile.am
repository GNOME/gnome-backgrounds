backgrounddir = $(datadir)/backgrounds/gnome

background_DATA =\
	FootFall.png \
	BlueMarbleWest.jpg \
	Terraform-blue.jpg \
	Terraform-green.jpg \
	Terraform-orange.jpg \
	Spaceflare.jpg \
	Spaceflare-nova.jpg \
	Spaceflare-supernova.jpg \
	SundownDunes.jpg \
	Stripes.jpg \
	Aqua.jpg \
	Blinds.jpg \
	FreshFlower.jpg \
	Garden.jpg \
	GreenMeadow.jpg \
	TwoWings.jpg \
	Wood.jpg \
	YellowFlower.jpg

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
