import sys,pygame
from pygame import Color,Vector2,draw,mouse
from math import *
from random import *
import copy

from pygame import mouse

pygame.init()

pens = []
getTicksLastFrame = 0
deltatime = 0
b1,b2 = 0,0
class Pen:
    pos,m,l,r,v,vc,point = Vector2(0),0,0,0,0,0,Vector2(0)
    def __init__(self,m,l,v,point) -> None:
        self.m = m
        self.l = l
        self.v = v
        self.vc = v
        self.point = point
        self.color = (randrange(255),randrange(255),randrange(255))
        self.a = 0
    def update(self):
        self.vc = copy.deepcopy(self.v)
        self.r += self.v * deltatime
        self.pos = self.point + (Vector2(cos((self.r + 90)),sin((self.r + 90))) * self.l)
        pygame.draw.circle(screen,self.color,self.pos,self.m)
        # pygame.draw.circle(screen,(255,0,0),self.point,2)

size = width,height = 600,600

screen = pygame.display.set_mode(size)

amount = 19
b = Pen(3,100/amount,0.5,Vector2(300,300))
pens.append(b)
for i in range(amount - 1):
    b = Pen(3,100/amount,0.5,b.pos)
    pens.append(copy.deepcopy(b))
while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    pygame.display.update()
    for i in pens:
        i.update()
    if(not mouse.get_pressed(3)[0]):
        screen.fill((0,0,0))
    