backgrounddir = $(datadir)/pixmaps/backgrounds/gnome/branded

background_DATA =\
	GNOME-Curves.png


metadata_in_files = gnome-branded.xml.in
metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = $(metadata_in_files:.xml.in=.xml)
@INTLTOOL_XML_RULE@

noinst_DATA = gnome-branded.xml.in
CLEANFILES = gnome-branded.xml gnome-branded.xml.in

EXTRA_DIST = $(background_DATA) gnome-branded.xml.in.in

gnome-branded.xml.in: gnome-branded.xml.in.in Makefile
	sed -e 's^\@datadir\@^$(datadir)^g' < $(srcdir)/gnome-branded.xml.in.in > gnome-branded.xml.in.tmp \
	&& mv gnome-branded.xml.in.tmp gnome-branded.xml.in

MAINTAINERCLEANFILES = \
	Makefile.in
