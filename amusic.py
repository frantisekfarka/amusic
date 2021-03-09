#!/usr/bin/python
# coding=utf-8

import subprocess
import dbus
import os
import time
import ewmh

NET_WM_FOCUSED = 287

bus = dbus.SessionBus()
proxy = bus.get_object(
    'org.freedesktop.ScreenSaver', '/org/freedesktop/ScreenSaver'
)
iface = dbus.Interface(proxy, 'org.freedesktop.ScreenSaver')

try:
    os.makedirs(os.path.expanduser("~") + "/.config/gnome-amusic")
except FileExistsError:
    # directory already exists
    pass




# inhibiting
# cookie = iface.Inhibit("amusic.py", "gnome-inhibit")
# print("Cookie: %i" % cookie)
# print("Inhibiting screensaver (pid: %d)" % os.getpid())


p = subprocess.Popen([
    'google-chrome',
    '--user-data-dir=' + os.path.expanduser('~') + '/.config/gnome-music',
    '--app=https://music.amazon.com',
    '--start-fullscreen'
])

time.sleep(2)

ewmh = ewmh.EWMH()
wins = filter(lambda w: ewmh.getWmPid(w) == p.pid, ewmh.getClientList())
win = list(wins)[0]

cookieSet = False
focused = False

while(p.poll() is None):
    if NET_WM_FOCUSED in ewmh.getWmState(win):
        focused = True
    else:
        focused = False

    # print('CookieSet: %s, focused: %b' , cookieSet , focused)
    if cookieSet is False and focused is True:
        cookie = iface.Inhibit("amusic.py", "gnome-inhibit")
        print("Inhibiting with cookie: %i" % cookie)
        cookieSet = True
    elif cookieSet is True and focused is False:
        print("UnInhibiting with cookie: %i" % cookie)
        iface.UnInhibit(cookie)
        cookieSet = False


    time.sleep(1)


print('Terminated')

if cookieSet is True:
    iface.UnInhibit(cookie)
print("UnInhibited with cookie: %i" % cookie)
