import sys,pygame
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
    
    draw.circle(screen,Color(192,100,20),Vector2(300,300),100)
    pygame.display.update()
    screen.fill((0,0,0))
