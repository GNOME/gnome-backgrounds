AC_INIT([gnome-backgrounds],
        [3.26.1],
        [http://bugzilla.gnome.org/browse.cgi?product=gnome-backgrounds],
        [gnome-backgrounds])

AC_CONFIG_MACRO_DIR([m4])

AM_INIT_AUTOMAKE([1.10 no-dist-gzip dist-xz])
AM_MAINTAINER_MODE([enable])

m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

GETTEXT_PACKAGE=gnome-backgrounds
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED([GETTEXT_PACKAGE], ["$GETTEXT_PACKAGE"], [The domain name to use with gettext.])

AM_GNU_GETTEXT_VERSION([0.19.8])
AM_GNU_GETTEXT([external])


AC_CONFIG_FILES([
Makefile
backgrounds/Makefile
po/Makefile.in
])
AC_OUTPUT
