EXTRA_DIST = 
CLEANFILES = 

python_PYTHON = $(builddir)/src/amusic.py


# The desktop files
desktopdir = $(datadir)/applications
desktop_DATA = $(builddir)/src/amusic.desktop

EXTRA_DIST = src/amusic.desktop

# The application icon
appicondir=$(datadir)/icons/hicolor/128x128/apps
appicon_DATA=amusic.png

amusic_ico_256='https://d5fx445wy2wpk.cloudfront.net/icons/amznMusic_favicon.png'

amusic_256.png:
	wget $(amusic_ico_256) -O $@

CLEANFILES += amusic_256.png

amusic.png: amusic_256.png
	convert -resize 128x128 $< $@

CLEANFILES += amusic.png


# Clean local automake fragments
clean-local:
	@rm -f config.status configure config.log
	@rm Makefile
	@rm -rf autom4te.cache/
	@rm -f aclocal.m4
	@rm -f compile install-sh missing Makefile.in
