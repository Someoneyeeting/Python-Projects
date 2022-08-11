import sys,pygame,keyboard
from pygame import Color,Vector2,draw,mouse,Rect,image
from math import *
from random import *
import copy

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 1280,768

dots = []
off = 0
offv = 0
screen : pygame.Surface
screen = pygame.display.set_mode(size)
t = 0
def lerp(v1,v2, d):
    return v1 * (1 - d) + v2 * d
a = 300
class Dot:
    global t
    global screen
    global off
    def __init__(self):
        seed(t % 5000)
        self.pos = Vector2(size)/2
        dir = randrange(0,360)
        self.dir = Vector2(cos(dir),sin(dir))
        self.v = 0
        dots.append(self)
    def update(self,delta):
        global a
        # self.v += delta * a
        self.pos += self.dir * a * delta
        if(self.pos.distance_to(Vector2(300,300)) > 500):
            dots.remove(self)
        o = 255 * self.pos.distance_to(Vector2(300,300)) / 300
        o = int(min(o,255))
        # ang = self.pos.angle_to(Vector2(300,300))
        # dist = self.pos.distance_to(Vector2(300,300))
        
        self.render = copy.deepcopy(self.pos)
        self.render -= Vector2(300,300)
        self.render = self.render.rotate(off)
        self.render += Vector2(300,300)
        draw.line(screen,Color(o,o,o),self.render,self.render + (Vector2(300,300) - self.render) / 5,2)
        # draw.circle(screen,Color(o,o,o),self.render,3)
        # draw.circle(screen,Color(o,o,o),self.pos,3)
        
timer = randrange(20,300) / 1000
recording = False

imagelist = []
filenamelist = [0]*10000
images = []
imagen = 0

def close():
    for i in range(len(images)):
        global screen
        image.save(images[i],"animation/image" + str(i) + ".png")
    sys.exit()

while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    timer -= deltatime
    if(timer <= 0):
        timer = randrange(10,40) / 1000
        for i in range(1):
            Dot()
    off += offv
    if(keyboard.is_pressed("right")):
        offv = lerp(offv,5,0.007)
        # print(off)
    elif(keyboard.is_pressed("left")):
        offv = lerp(offv,-5,0.007)
    else:
        offv = lerp(offv,0,0.01)
        # print(off)
    if(keyboard.is_pressed("up")):
        a += 0.01
    elif(keyboard.is_pressed("down")):
        a -= 0.01
    # a += sin(t * 0.1) * 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT: close()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                recording = not recording
                print(pygame.image)
    for i in dots:
        i.update(deltatime)
    if(recording and len(images) < 100):
        # filenamelist[image] = "animation/pic" + str(image) + ".png"
        # pygame.image.save(screen, filenamelist[image])
        if(screen.copy() in images):
            close()
        images.append(screen.copy())
        pygame.display
        # imagen += 1
    pygame.display.update()
    screen.fill((0,0,0))
