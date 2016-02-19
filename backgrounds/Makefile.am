backgrounddir = $(datadir)/backgrounds/gnome

background_DATA =\
	adwaita-day.jpg \
	adwaita-lock.jpg \
	adwaita-morning.jpg \
	adwaita-night.jpg \
	adwaita-timed.xml \
	Blinds.jpg \
	Bokeh_Tails.jpg \
	Chmiri.jpg \
	Dark_Ivy.jpg \
	Fabric.jpg \
	Flowerbed.jpg \
	FootFall.png \
	Godafoss_Iceland.jpg \
	Mirror.jpg \
	Road.jpg \
	Sandstone.jpg \
	Stones.jpg \
	Terraform-green.jpg \
	Waves.jpg

metadata_in_files = gnome-backgrounds.xml.in adwaita.xml.in
metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = $(metadata_in_files:.xml.in=.xml)
@INTLTOOL_XML_RULE@

noinst_DATA = gnome-backgrounds.xml.in adwaita.xml.in
CLEANFILES = gnome-backgrounds.xml gnome-backgrounds.xml.in adwaita.xml adwaita.xml.in adwaita-timed.xml

EXTRA_DIST = $(background_DATA) gnome-backgrounds.xml.in.in adwaita.xml.in.in adwaita-timed.xml.in

edit = sed -e 's|@BACKGROUNDDIR[@]|$(backgrounddir)|g'

adwaita.xml.in: adwaita.xml.in.in Makefile
	$(AM_V_GEN) sed -e 's^\@datadir\@^$(datadir)^g' < $(srcdir)/adwaita.xml.in.in > adwaita.xml.in.tmp \
	&& mv adwaita.xml.in.tmp adwaita.xml.in

adwaita-timed.xml: adwaita-timed.xml.in Makefile
	$(AM_V_GEN) sed -e 's^\@datadir\@^$(datadir)^g' < $(srcdir)/adwaita-timed.xml.in > adwaita-timed.xml.tmp \
	&& mv adwaita-timed.xml.tmp adwaita-timed.xml

gnome-backgrounds.xml.in: gnome-backgrounds.xml.in.in Makefile
	$(edit) $< >$@

MAINTAINERCLEANFILES = \
	Makefile.in

-include $(top_srcdir)/git.mk
