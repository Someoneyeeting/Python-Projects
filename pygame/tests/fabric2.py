import sys,pygame
from pygame import Color,Vector2,draw,mouse
from math import *
from random import *
import copy

from pygame import mouse

def dist(a : Vector2,b : Vector2) -> float:
    return sqrt(((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))

def dir(a : Vector2,b : Vector2):
    return Vector2(cos(b.x - a.x),sin(b.y - a.y))

def norm(a : Vector2):
    len = dist(a,Vector2(0,0))
    return a / len

pygame.init()

getTicksLastFrame = 0
deltatime = 0

mouseup = False
mousedown = False
screen = 0
points = []
global lid
lid = 1
l,s = 1,200
amount = 100
scolor = Color(randrange(0,255),randrange(0,255),randrange(0,255))
fcolor = Color(randrange(0,255),randrange(0,255),randrange(0,255))
class Point:
    pos,linked,color,v,id = 0,0,0,0,0
    def __init__(self,pos,id) -> None:
        self.pos = copy.deepcopy(pos)
        self.linked = []
        self.v = Vector2(0,0)
        self.color = Color(randrange(0,255),randrange(0,255),randrange(0,255))
        self.id = copy.deepcopy(id)
        self.fixed = False
        #self.fixed = True if self.id == 1 else False
        # self.fixed = False
        # if(self.id != 1):
        #     self.link(points[len(points) - 1])
    def link(self,point):
        if(point in self.linked):
            return
        self.linked.append(point)
        point.linked.append(self)
    def update(self):
        sf = Vector2(0,0)
        for i in self.linked:
            if(not self.fixed):
                if(self.pos == i.pos):
                    self.pos += Vector2(randrange(-2,2))
                sf += (norm(i.pos - self.pos)) * ((dist(self.pos,i.pos) - l) * s) / (2 if sf == Vector2(0,0) else 1)
            if i.id > self.id:
                draw.line(screen,scolor.lerp(fcolor,self.id / amount),self.pos,i.pos)
        # if(id == 1 or id == amount):
        #     draw.circle(screen,self.color,self.pos,5)
        # self.v.y += 0.98
        # if(mousedown and mouse.get_pressed()[0]):
        #     self.v += ((self.pos - mouse.get_pos()) / dist(self.pos,Vector2(mouse.get_pos()[0],mouse.get_pos()[1]))) * 2
        # if(self.pos.y + (self.v.y * deltatime) > 600 or self.pos.y + (self.v.y * deltatime) < 0):
        #     self.v.y *= -1
        # if(self.pos.x + (self.v.y * deltatime) > 600 or (self.v.y * deltatime) < 0):
        #     self.v.x *= -1
        
        if(not self.fixed):
            self.pos += sf * deltatime
            # self.pos.y += 0.98 if self.pos.y + 0.98 < 550 else 550 - self.pos.y
        
        if(dist(self.pos,Vector2(mouse.get_pos())) < 10):
            if(mousedown):
                if(mouse.get_pressed()[0]):
                    self.moving = True
                elif(mouse.get_pressed()[2]):
                    self.fixid = not self.fixed
        if(mouseup): self.moving = False
        if(self.moving):self.pos = Vector2(mouse.get_pos())

for i in range(amount):
    points.append(Point(Vector2(randrange(100,500),randrange(100,500)) if lid == 1 or amount else Vector2(300,300),lid))
    lid += 1

for i in range(len(points)):
    if(i + 1 < len(points)):
        points[i].link(points[i+1])

size = width,height = 600,600

screen = pygame.display.set_mode(size)

while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    mouseup = False
    mousedown = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP : mouseup = True
        if event.type == pygame.MOUSEBUTTONDOWN : mousedown = True
    if mousedown and mouse.get_pressed()[1]:
        for i in points:
            if not i.fixed:
                i.pos = Vector2(300,300) + Vector2(randrange(-60,60),randrange(-60,60))
        scolor = Color(randrange(0,255),randrange(0,255),randrange(0,255))
        fcolor = Color(randrange(0,255),randrange(0,255),randrange(0,255))
    for i in points:
        try:
            i.update()
        except:
            pass
    pygame.display.update()
    screen.fill((0,0,0))
