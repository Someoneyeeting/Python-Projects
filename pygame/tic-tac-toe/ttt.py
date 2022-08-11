import sys,pygame,keyboard,mouse
from pygame import Color,Vector2,draw,mouse
from math import *
from random import *
import copy

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600

screen = pygame.display.set_mode(size)


while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((200,200,200))
    draw.line(screen,Color(20,20,20),Vector2(200,0),Vector2(200,600),10)
    draw.line(screen,Color(20,20,20),Vector2(400,0),Vector2(400,600),10)
    draw.line(screen,Color(20,20,20),Vector2(0,200),Vector2(600,200),10)
    draw.line(screen,Color(20,20,20),Vector2(0,400),Vector2(600,400),10)
    pygame.display.update()
