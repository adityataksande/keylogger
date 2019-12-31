import pynput

from pynput.keyboard import Key, Listener

with Listener(on_press=onpress,on_release=onrelease)