from random import *
import time
import keyboard

key = "`1234567890-=qwertyuiop[]asdfghjklQWERTYUIOPASDFGHJKLZXCVBNM;'\zxcvbnm,./"
keys = []

for i in key:
    keys.append(i)

print("ctrl + e to stop")

while not keyboard.is_pressed("ctrl+e"):
    for i in keys:
        if(keyboard.is_pressed(i)):
            keyboard.press_and_release("backspace")
            keyboard.press_and_release(keys[randrange(0,len(keys))])
            time.sleep(0.3)
            break