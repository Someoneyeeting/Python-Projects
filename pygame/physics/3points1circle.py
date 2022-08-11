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

screen = pygame.display.set_mode(size)

p1,p2,p3,cp,cd = Vector2(0,0),Vector2(0,0),Vector2(0,0),Vector2(0,0),100


while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    draw.circle(screen,Color(255,255,255),p1,4)
    draw.circle(screen,Color(255,255,255),p2,4)
    draw.circle(screen,Color(255,255,255),p3,4)
    draw.circle(screen,Color(255,255,255),cp,cd,10)
    pygame.display.update()
    screen.fill((0,0,0))
