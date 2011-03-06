backgrounddir = $(datadir)/backgrounds/gnome/abstract

background_DATA = \
	Flow.png \
	Gulp.png \
	Silk.png \
	Spring.png \
	Waves.png


metadata_in_files = gnome-abstract.xml.in
metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = $(metadata_in_files:.xml.in=.xml)
@INTLTOOL_XML_RULE@

noinst_DATA = gnome-abstract.xml.in
CLEANFILES = gnome-abstract.xml gnome-abstract.xml.in

EXTRA_DIST = $(background_DATA) gnome-abstract.xml.in.in

edit = sed \
	-e 's|@BACKGROUNDDIR[@]|$(backgrounddir)|g'

gnome-abstract.xml.in: gnome-abstract.xml.in.in Makefile
	$(edit) $< >$@

MAINTAINERCLEANFILES = \
	Makefile.in

-include $(top_srcdir)/git.mk
