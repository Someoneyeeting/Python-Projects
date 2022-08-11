from PIL import Image
import math
import random
from datetime import datetime

def dist(x : float,y : float,x1 : float,y2 : float):
    return (x1 - x) * (x1 - x) + (y2 - y) * (y2 - y)

bg = Image.new('RGB',(1360,768),(0,0,0))
pixels = bg.load()
noise = []
for i in range(7):
    noise.append((random.randrange(0,1360),random.randrange(0,768)))
colors = ((random.randrange(random.randrange(0,100),random.randrange(100,255)),random.randrange(random.randrange(0,100),random.randrange(100,255))),(random.randrange(random.randrange(0,100),random.randrange(100,255)),random.randrange(random.randrange(0,100),random.randrange(100,255))),(random.randrange(random.randrange(0,100),random.randrange(100,255)),random.randrange(random.randrange(0,100),random.randrange(100,255))))
random.seed(datetime.now())
for x in range(1360):
    for y in range(768):
        dis = math.inf
        for i in noise:
            distn = dist(x,y,i[0],i[1]) / 255
            distn /= 100
            dis = min(dis,distn)
        pixels[x,y] = (abs(int(colors[0][1] - dis * colors[0][0])),abs(int(colors[1][1] - dis * colors[1][0])),abs(int(colors[2][1] - dis * colors[2][0])))
        # pixels[x,y] = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
bg.show()
bg.save("E://python/background.png")
print("done")