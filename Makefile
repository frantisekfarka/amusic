AMUSIC_ICO_256='https://d5fx445wy2wpk.cloudfront.net/icons/amznMusic_favicon.png'

EXECUTABLES = wget convert google-chrome
DEPS := $(foreach exec,$(EXECUTABLES),\
        $(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH")))


ico: amusic.png

amusic.png:amusic_128.png
	cp $< $@

amusic_256.png:
	wget $(AMUSIC_ICO_256) -O $@

amusic_128.png: amusic_256.png
	convert -resize 128x128 $< $@

clean:
	rm -f amusic_256.png amusic_128.png amusic.png
