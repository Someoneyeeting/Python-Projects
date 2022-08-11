import sys,pygame,random
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
import copy
import keyboard

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0
t = 0

size = width,height = 600,600
screen = pygame.display.set_mode(size)

dots = []
center = Vector2(width/2,height/2)
dotcount = 1500
limiter = 1/60


class Dot:
    pos,rad,ang = Vector2(0,0),0,0
    def __init__(self,ang,rad):
        self.rad = rad
        self.ang = ang
        self.id = len(dots)
        dots.append(self)
        
    def update(self):
        self.rad  = (self.id / (dotcount - 1)) * 150
        self.ang = 2 * pi * turn * self.id
        self.pos = center + (Vector2(cos(self.ang * (pi / 180)),sin(self.ang * (pi / 180))) * self.rad)
        
        col = (int((self.id / dotcount) * (255))) + self.ang
        b = int(col % 255)
        b = int(b + ((b + 20) % 255) / 2) % 255
        g = int((col + (255 / 3)) % 255) 
        g = int(g + ((g + 20) % 255) / 2)% 255
        r = int((col + ((255 /3) * 2)) % 255)
        r = int(r + ((r + 20) % 255) / 2)% 255
        try:
            color = Color(r,g,b)
            draw.circle(screen,color,self.pos,2)
        except:
            print(r,g,b)
        mi.x = min(self.pos.x,mi.x)
        mi.y = min(self.pos.y,mi.y)
        ma.x = max(self.pos.x,ma.x)
        ma.y = max(self.pos.y,ma.y)


for i in range(dotcount):
    Dot(0,0)

turn = 0

while 1:
    t = pygame.time.get_ticks()
    if(t % limiter < 10):
        mi,ma = Vector2(600,600),Vector2(0,0)
        deltatime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # print(1/deltatime)
        # dots = []
        # dist = ((i / 2300) * 60) + ((i * 5) % 240)
        # Dot((randrange(-10,10) / 180 * pi) + (i/dotcount) * 360,dist)
        tu = (1.161 / dotcount) 
        if(keyboard.is_pressed("right")):
            turn += tu
        elif(keyboard.is_pressed("left")):
            turn -= tu
        if(keyboard.is_pressed("space")):
            print(turn)
        for i in dots:
            i.update()
        # draw.rect(screen,Color(255,255,255),Rect(Vector2(mi.x,mi.y),Vector2(ma.x - mi.x,ma.y - mi.y)),2)
        pygame.display.update()
        screen.fill((0,0,0))
