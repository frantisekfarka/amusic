AC_INIT([amusic],[0.0.1],[franisek@farka.eu])
AM_INIT_AUTOMAKE
AC_CONFIG_FILES([Makefile])
AM_PATH_PYTHON

AC_CHECK_PROG(CONVERT, convert, yes) 
if test "$CONVERT" != "yes" ; then
    AC_MSG_ERROR([Could not locate ImageMagick convert.])
fi
AC_OUTPUT
