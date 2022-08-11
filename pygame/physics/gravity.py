import sys,pygame,keyboard
from turtle import distance
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
import copy

from pygame import mouse

pygame.init()

scale = pow(10,-30)
getTicksLastFrame = 0
deltatime = 0
G = (6.67 * pow(10,5.5))  


size = width,height = 600,600

screen = pygame.display.set_mode(size)


circles = []

line = []

class Circle:
    pos,v,a,cv,ca,m,color = Vector2(0,0),Vector2(0,0),Vector2(0,0),Vector2(0,0),Vector2(0,0),0,0

    def __init__(self,pos,m,r) -> None:
        self.pos = pos
        self.m = m
        self.v = Vector2(0,0)
        self.a = Vector2(0,0)
        self.color = Color(randrange(0,255),randrange(0,255),randrange(0,255))
        self.f = Vector2(0,0)
        self.fixed = False
        self.r = r

    def update(self,delta):
        if(not self.fixed):
            pass
            self.cv = copy.deepcopy(self.v)
            self.ca = copy.deepcopy(self.a)
            self.a = self.f/self.m
            self.f = Vector2(0)
            self.v += self.a * delta
            self.pos += self.v * delta
            for i in circles:
                if i == self:
                    continue
                self.f += (G * (self.m * i.m / self.pos.distance_squared_to(i.pos))) * (i.pos - self.pos).normalize()
                
            # if(self.pos.x - self.m < 0):
            #     self.pos.x = self.m
            #     self.v.x *= -1
            # if(self.pos.x + self.m > 600):
            #     self.pos.x = 600 - self.m
            #     self.v.x *= -1

            # if(self.pos.y - self.m < 0):
            #     self.pos.y = self.m
            #     self.v.y *= -1
            # if(self.pos.y + self.m > 600):
            #     self.pos.y = 600 - self.m
            #     self.v.y *= -1
        line.append()
        draw.circle(screen,self.color,self.pos,self.r)

circles.append(Circle(Vector2(500,300),(5.972 * pow(10,24)) * scale,10))
circles[0].v = Vector2(0,-130)
# circles.append(Circle(Vector2(500,350),(7.34767309 * pow(10,22)) * scale,5))
# circles[1].v = Vector2(-100,0)
circles.append(Circle(Vector2(300,300),(1.989 * pow(10,30)) * scale,30))
circles[-1].fixed = True

while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    for i in circles:
        i.update(deltatime)
    pygame.display.update()
    screen.fill((0,0,0))
