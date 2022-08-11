import sys
from PIL import Image
import time
import keyboard
from PIL import ImageGrab
true = True
false = False
black = (17,17,17)
rec1 = {544,474,546,476}
rec2 = {626,474,628,476}
rec3 = {711,474,713,476}
rec4 = {800,474,802,476}

playing = true
while playing:
    if(keyboard.is_pressed("e")):
        playing = false
    
    rec1image = ImageGrab.grab(rec1)
    rec2image = ImageGrab.grab(rec2)
    rec3image = ImageGrab.grab(rec3)
    rec4image = ImageGrab.grab(rec4)

    rec1data = list(rec1image.getdata())
    rec2data = list(rec2image.getdata())
    rec3data = list(rec3image.getdata())
    rec4data = list(rec4image.getdata())
    
    if(black in rec1data):
        keyboard.press_and_release("a")
        print(1)
    if(black in rec2data):
        keyboard.press_and_release("s")
        print(2)
    if(black in rec3data):
        keyboard.press_and_release("d")
        print(3)
    if(black in rec4data):
        keyboard.press_and_release("f")
        print(4)
    
