import sys,pygame
from pygame import Color,Vector2,draw,mouse
from math import *
from random import *
import copy

from pygame import mouse

def dest(b1,b2):
    return (((b2.pos.x + b2.v.x) - (b1.pos.x + b1.v.x)) ** 2) + (((b2.pos.y + b2.v.y) - (b1.pos.y + b1.v.y)) ** 2)

balls = []
class Ball:
    def __init__(self,pos,rad,v,color) -> None:
        self.pos = pos
        self.rad = rad
        self.v = v
        self.cv = self.v
        self.color = color
    def update(self):
        self.cv = copy.copy(self.v)
        self.v.x *= 1.1 if abs(self.v.x) < 0.1 else 1
        self.v.y *= 1.1 if abs(self.v.y) < 0.1 else 1
        for i in balls:
            if(i == self):
                continue
            colx,coly = i.pos.x - self.pos.x , i.pos.y - self.pos.y
            if((self.rad + i.rad) ** 2 > dest(self,i)):
                if(abs(colx) > abs(coly)):
                    self.v.x *= -(self.rad / i.rad if self.rad / i.rad < 1 else 1 - (self.rad / i.rad))
                else:
                    self.v.y *= -(self.rad / i.rad if self.rad / i.rad < 1 else 1 - (self.rad / i.rad))
        #         self.v.x = (self.cv.x * (self.rad - i.rad) + (2 * i.rad * i.cv.x)) / (self.rad + i.rad)
        #         self.v.y = (self.cv.y * (self.rad - i.rad) + (2 * i.rad * i.cv.y)) / (self.rad + i.rad)
        # for i in balls:
        #     if(i != self):
        off = randrange(-5,5)
        try:
            if(self.color.r + off > 255):
                self.color.r = off
            elif(self.color.r + off < 0):
                self.color.r = 255 + off
            else:
                self.color.r += 255
                
            off = randrange(-5,5)
            if(self.colog.g + off > 255):
                self.colog.g = off
            elif(self.colog.g + off < 0):
                self.colog.g = 255 + off
            else:
                self.colog.g += 255
                
            off = randrange(-5,5)
            if(self.colob.b + off > 255):
                self.colob.b = off
            elif(self.colob.b + off < 0):
                self.colob.b = 255 + off
            else:
                self.colob.b += 255
        except:
            pass     
        # self.v += (mouse.get_pos() - self.pos) * 0.1
        while(self.pos.y + self.v.y - self.rad < 0 or self.pos.y + self.v.y + self.rad > 600):
            self.v.y *= -1
        while(self.pos.x + self.v.x - self.rad < 0 or self.pos.x + self.v.x + self.rad > 600):
            self.v.x *= -1
        self.pos += self.v

pygame.init()


size = width,height = 600,600

screen = pygame.display.set_mode(size)

for i in range(30):
    ball = Ball(Vector2(randrange(20,580),randrange(20,580)),randrange(5,14),Vector2(float(randrange(-10,10)) / 5.0,float(randrange(-10,10)) / 10.0),Color(randrange(255),randrange(255),randrange(255)))
    balls.append(ball)
getTicksLastFrame = 0
time = 0
while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    time += deltatime
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    for i in balls:
        i.update()
    # screen.fill((240,255,255))
    for i in balls:
        draw.circle(screen,i.color,i.pos,i.rad)
    pygame.display.update()
    screen.fill((0,0,0))
    # if(not (time > 0.4)):
    #     time = 0