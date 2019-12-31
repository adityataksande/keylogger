import pynput

from pynput.keyboard import Key, Listener

def onpress(key):
    global keys, count
    print("(0) pressed".format(key))

def onrelease(key):
    if key == Key.esc:
        return False


with Listener(onpress=onpress, onrelease=onrelease) as listener:
    listener.join()
