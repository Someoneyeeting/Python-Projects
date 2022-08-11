import sys,pygame
from pygame import Color,Vector2,draw,mouse
from math import *
from random import *
import copy
from copy import deepcopy

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600

dots = 1

dot = []

for i in range(dots):
    dot.append(0)

wave = []
screen = pygame.display.set_mode(size)

while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    # rot += 0.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    prev = Vector2(100,300)
    pos = Vector2(0,0)
    for i in range(dots):
        rot = dot[i]
        rot += 0.006
        pos = (Vector2(tan(rot * (i + 1)),sin(rot * (i + 1))) * 5 * dots / (i + 1)) + prev
        dot[i] = rot
        draw.line(screen,Color(255,255,255),pos,prev,2)
        prev = deepcopy(pos)
    if(dot[0] >= pi * 2):
        dot[0] -= pi*2
        dots += 1
        dot.append(0)
    else:
        wave.append(pos)
    # for i in wave:
    #     i.x += 1
    #     if(i.x > 600):
    #         wave.remove(i)
    if(len(wave) > 1):
        draw.lines(screen,Color(255,255,255),False,wave,1)
    pygame.display.update()
    screen.fill((0,0,0))
