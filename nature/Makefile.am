backgrounddir = $(datadir)/backgrounds/gnome/nature

background_DATA =\
	FootFall.jpg \
	Terraform-blue.jpg \
	Terraform-green.jpg \
	Terraform-orange.jpg \
	Spaceflare.jpg \
	Spaceflare-nova.jpg \
	Spaceflare-supernova.jpg \
	SundownDunes.jpg \
	Aqua.jpg \
	Blinds.jpg \
	FreshFlower.jpg \
	Garden.jpg \
	GreenMeadow.jpg \
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

edit = sed \
	-e 's|@BACKGROUNDDIR[@]|$(backgrounddir)|g'

gnome-nature.xml.in: gnome-nature.xml.in.in Makefile
	$(edit) $< >$@

MAINTAINERCLEANFILES = \
	Makefile.in

-include $(top_srcdir)/git.mk
