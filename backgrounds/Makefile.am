backgrounddir = $(datadir)/backgrounds/gnome

background_DATA =\
	Aqua.jpg \
	Blinds.jpg \
	BlueMarbleWest.jpg \
	Chmiri.jpg \
	FootFall.png \
	FreshFlower.jpg \
	Garden.jpg \
	GreenMeadow.jpg \
	Spaceflare.jpg \
	Spaceflare-nova.jpg \
  Stamps.jpg \
	Stripes.jpg \
	Stripes34.jpg \
	SundownDunes.jpg \
	Terraform-blue.jpg \
	Terraform-green.jpg \
	Terraform-orange.jpg \
	TwoWings.jpg \
	UnderLit.jpg \
	Wood.jpg \
	YellowFlower.jpg \
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
