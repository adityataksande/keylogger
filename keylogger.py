from pynput.keyboard import Key, Listener

def onpress(key):
    print("(0) pressed".format(key))

def onrelease(key):
    if key == Key.esc:
        return False