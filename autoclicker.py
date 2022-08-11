import mouse
import time

cps = 1000
while True:
    if(mouse.is_pressed(mouse.X2)):
        mouse.click(mouse.LEFT)
        time.sleep(1/cps)