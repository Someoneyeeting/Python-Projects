from pynput.keyboard import Key,Listener
from pynput.mouse import Button,Controller
import time
from copy import deepcopy

mouse = Controller()


def on_press(key):
    mp = (mouse.position[0],mouse.position[1])
    if(key == Key.space):
        mouse.move(600 - mouse.position[0], 622 - mouse.position[1])
        off = (mouse.position[0] - 600,mouse.position[1] - 622)
        mouse.move(off[0],off[1])
        time.sleep(0.07)
        mouse.move(600 - mouse.position[0], 760 - mouse.position[1])
        time.sleep(0.01)
        #time.sleep(0.05)
        off = (mouse.position[0] - 600,mouse.position[1] - 760)
        mouse.move(mp[0] - mouse.position[0], mp[1] - mouse.position[1])
        mouse.move(off[0],off[1])
        
def on_release(key):
    return


with Listener(
    on_press = on_press,
    on_release = on_release
    ) as lis:
        lis.join()
        
