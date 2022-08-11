from pynput.mouse import Button, Controller
from pynput.keyboard import Listener,Key,KeyCode
from pynput import keyboard


v = [0,0]

def on_keyboard(key):
    global v
    v = [0,0]
    if key == KeyCode.from_char("j"):
        v[0] = -10
    if(key == KeyCode.from_char("l")):
        v[0] = 10
    if(key == KeyCode.from_char("i")):
        v[1] = -10
    if(key == KeyCode.from_char("k")):
        v[1] = 10

with Listener(on_press=on_keyboard) as listener:
    listener.join()
mouse = Controller()
mouse.move(v[0],v[1])