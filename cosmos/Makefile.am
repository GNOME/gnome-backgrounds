NULL =

backgrounddir = $(datadir)/pixmaps/backgrounds/gnome/cosmos

BACKGROUNDS = \
	blue-marble-west.jpg	\
	cloud.jpg 		\
	comet.jpg 		\
	earth-horizon.jpg	\
	galaxy-ngc3370.jpg	\
	helix-nebula.jpg	\
	jupiter.jpg		\
	sombrero.jpg		\
	whirlpool.jpg		\
	$(NULL)

background_DATA =		\
	$(BACKGROUNDS)		\
	background-1.xml	\
	$(NULL)

gnome-cosmos.xml.in: gnome-cosmos.xml.in.in Makefile
	$(edit) $< >$@

background-1.xml: background-1.xml.in Makefile
	$(edit) $< >$@

metadata_in_files = gnome-cosmos.xml.in
metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = $(metadata_in_files:.xml.in=.xml)
@INTLTOOL_XML_RULE@

edit = sed \
	-e 's|@BACKGROUNDDIR[@]|$(backgrounddir)|g'

EXTRA_DIST =			\
	CREDITS 		\
	$(BACKGROUNDS)		\
	background-1.xml.in	\
	gnome-cosmos.xml.in.in	\
	$(NULL)

CLEANFILES = \
	gnome-cosmos.xml.in		\
	$(NULL)

DISTCLEANFILES = \
	gnome-cosmos.xml		\
	background-1.xml		\
	$(NULL)

MAINTAINERCLEANFILES =                  \
	*~				\
	Makefile.in			\
	$(NULL)
