from PIL import Image
from random import *
import math
import colorsys


def to_hsv(pixel):
  conv = pixel[0] / 255.0,pixel[1] / 255.0,pixel[2] / 255.0
  hsv = colorsys.rgb_to_hsv(conv[0],conv[1],conv[2])
  conv = hsv[0] * 255.0,hsv[1] * 255.0,hsv[2] * 255.0
  return conv

def to_rgb(pixel):
  conv = pixel[0] / 255.0,pixel[1] / 255.0,pixel[2] / 255.0
  hsv = colorsys.hsv_to_rgb(conv[0],conv[1],conv[2])
  conv = hsv[0] * 255.0,hsv[1] * 255.0,hsv[2] * 255.0
  return conv

img1,img2 = 0,0
img1 = Image.open("1.png")
img2 = Image.open("2.png")

w1,h1 = img1.size
w2,h2 = img2.size

w,h = max(w1,w2),max(h1,h2)

big,small = 0,0

big = img2 
small = img1 
if(w1 + h1 > w2 + h2):
  big,small = small,big
ratio = (small.size[0]/big.size[0],small.size[1]/big.size[1])


a = big.load()
b = small.load()
hsv = big.convert("HSV").load()
for x in range(0,w):
  for y in range(0,h):
    ax,ay = x,y
    ax = max(0,min(w1 - 1,ax))
    ay = max(0,min(h1 - 1,ay))
    pa = a[ax,ay]
    pb = b[int(ax * ratio[0]),int(ay * ratio[1])]
    # hs = hsv[ax,ay]
    ha = to_hsv(pa)
    hb = to_hsv(pb)
    
    # hab = ((ha[0] + hb[0]) / 2,(ha[1] + hb[1]) / 2,(ha[2] + hb[2]) / 2)
    
    hab = ((ha[0]),ha[2],ha[1])
    
    final = to_rgb(hab)
    
    pc = final
    
    pc = (int(pc[0]),int(pc[1]),int(pc[2]))
    
    a[x,y] = pc
    # a[x,y] = int(v[randrange(0,3)]) , int(v[randrange(0,3)]) , int(v[randrange(0,3)])
    # a[x,y] = int((pa[0] + pb[0]) / 2),int((pa[1] + pb[1]) / 2),int((pa[2] + pb[2]) / 2)
big.save("done.png")
