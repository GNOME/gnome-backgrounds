backgrounddir = $(datadir)/pixmaps/backgrounds/gnome/abstract

background_DATA =\
	due-alt.jpg \
	intenso-alt.jpg \
	onda-alt.jpg \
	raggi-alt.jpg \
	scie-alt.jpg \
	due.jpg \
	intenso.jpg \
	onda.jpg \
	raggi.jpg \
	scie.jpg


metadata_in_files = gnome-abstract.xml.in
metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = $(metadata_in_files:.xml.in=.xml)
@INTLTOOL_XML_RULE@

noinst_DATA = gnome-abstract.xml.in
CLEANFILES = gnome-abstract.xml gnome-abstract.xml.in

EXTRA_DIST = $(background_DATA)

gnome-abstract.xml.in: gnome-abstract.xml.in.in Makefile
	sed -e 's^\@datadir\@^$(datadir)^g' < gnome-abstract.xml.in.in > gnome-abstract.xml.in.tmp \
	&& mv gnome-abstract.xml.in.tmp gnome-abstract.xml.in

MAINTAINERCLEANFILES = \
	Makefile.in
