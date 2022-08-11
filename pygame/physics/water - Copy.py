from decimal import Clamped
import sys,pygame,keyboard
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
import copy

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600
fps = 1/500
spring = 100000
circles = []
class Circle:
    pos,v,a = Vector2(0,0),Vector2(0,0),Vector2(0,0)
    m = 10
    draged = False
    forces = []
    clr = Color(0,0,0)
    def __init__(self,pos,clr):
        self.pos = pos
        self.clr = clr
        self.v = Vector2(randrange(-10,10),randrange(-10,10))
        circles.append(self)
    
    def drag(self):
        if(self.pos.distance_to(Vector2(mouse.get_pos())) < self.m):
            self.draged = True
    def acfrom(self,point):
        if(self.pos == point):
            self.pos.x+=0.001
        dist = self.pos.distance_to(point)
        return((self.pos - point).normalize() * (-(dist - 200) * spring))
        return Vector2(0,0)
    def checkforces(self):
        for circle in circles:
            if(circle == self):
                continue
            
           #if(self.pos.y > 500):
           #    self.forces.append(self.acfrom(Vector2(self.pos.x,730)))
            
           #if(self.pos.x > 500):
           #    self.forces.append(self.acfrom(Vector2(760,self.pos.y)))
               
           #if(self.pos.x < 100):
            #   self.forces.append(self.acfrom(Vector2(-130,self.pos.y)))
           
            self.forces.append(self.acfrom(circle.pos))
        
    def update(self,screen):
        if(mouse.get_pressed()[0]):
            self.forces.append(self.acfrom(Vector2(mouse.get_pos())) * 5)
            self.draged = False
        # if(self.draged):
        #     self.pos = Vector2(mouse.get_pos())
        #     self.v = Vector2(0,0)
        self.a = Vector2(0,11)
        for force in self.forces:
            self.a += (force * fps**2) / self.m
        self.v += self.a
        if(self.pos.y + (self.v.y * fps) + self.m >= 600 or self.pos.y + (self.v.y * fps) + self.m <= 0):
            self.pos.y -= self.v.y * fps
            self.v.y *= 0
        if(self.pos.x + (self.v.x * fps) + self.m >= 600 or self.pos.x + (self.v.x * fps) + self.m <= 0):
            self.pos.x -= self.v.x * fps
            self.v.x *= 0
        self.pos += self.v * fps
        draw.circle(screen,self.clr,self.pos,self.m)
        self.forces = []


screen = pygame.display.set_mode(size)

for i in range(50):
    Circle(Vector2(randrange(20,580),randrange(20,580)),Color(randrange(255),randrange(255),randrange(255)))

while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                for circle in circles:
                    circle.v = Vector2(0,0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for circle in circles:
                circle.drag()
    for circle in circles:
        circle.update(screen)
    for circle in circles:
        circle.checkforces()
    pygame.display.update()
    screen.fill((0,0,0))
