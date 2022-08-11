from turtle import goto
from PIL import Image
import time,mouse,keyboard,math

mousepos = (56,173)
imgsize = (500,500)

image = Image.open("image2.png")

size = image.size

scale = 0
if(size[0] > size[1]):
    scale = imgsize[0]/size[0]
else:
    scale = imgsize[1]/size[1]

pixels = image.load()
print(int(size[0] / scale),int(size[1] / scale))
print(size)
keyboard.wait("q")
done = False

for y in range(0,size[1],math.ceil(1/scale)):
    if(done):
        break
    for x in range(0,size[0],math.ceil(1/scale)):
        mouse.move(mousepos[0] + (x * scale),mousepos[1] + (y * scale))
        pix = pixels[x,y]
        gray = pix[0] + pix[1] + pix[2]
        gray /= 3
        if(gray > 200):
            mouse.press()
        else:
            mouse.release()
        done = keyboard.is_pressed("w")
    mouse.release()
        
        
        