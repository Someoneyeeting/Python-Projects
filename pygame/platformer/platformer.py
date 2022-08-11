import sys,pygame
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
import copy
# import Box

from pygame import mouse
def Rect.isCol(self,box : Rect):
    return True

deltatime = 0

pygame.init()

size = width,height = 600,600

screen = pygame.display.set_mode(size)
getTicksLastFrame = 0


box = Rect(Vector2(300,300),Vector2(100,100))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    screen.fill((0,0,0))
    draw.rect(screen,Color(100,100,100),box)
    pygame.display.update()