import sys
from PIL import Image
import pyscreenshot as ss
import time
import keyboard
from PIL import ImageGrab
# time.sleep(2)
playing = True
loop = 0
off = 40
while playing:
    if (keyboard.is_pressed("e")):
        playing = False
    start = time.time()
    gray = (83,83,83)
    box1 = (435 + off,272,448 + off,295)
    box2 = (448 + off,272,461 + off,295)
    restartbutton = (580,224,587,225)

    box1path = r"E:\\pybot\box1.png"
    box2path = r"E:\\pybot\box2.png"
    restartpath = r"E:\\pybot\restart.png"

    box1image = ImageGrab.grab(bbox = box1)
    box2image = ImageGrab.grab(bbox = box2)
    restartimage = ImageGrab.grab(bbox = restartbutton)
    
    
    # box1open = Image.open(box1path,'r')
    # box2open = Image.open(box2path,'r')
    # restartopen = Image.open(restartpath,'r')

    box1data = list(box1image.getdata())
    box2data = list(box2image.getdata())
    restartdata = list(restartimage.getdata())
    if(gray in box1data):
        if(gray in box2data):
            keyboard.press("up")
            time.sleep(1)
            keyboard.release("up")
        else:
            keyboard.press("up")
            time.sleep(0.3)
            keyboard.release("up")
        box1image.save(box1path)
        box2image.save(box2path)
        restartimage.save(restartpath)

    if(gray in restartdata):
        keyboard.press_and_release("up")
        box1image.save(box1path)
        box2image.save(box2path)
        restartimage.save(restartpath)

    end = time.time()
    print(end - start)
