import sys,pygame,keyboard,copy
from Corner import *
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600

screen = pygame.display.set_mode(size)

f = Corner()


while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    mp = Vector2(mouse.get_pos())
    f.pos = Vector3((300,300,0))
    if(mp.x != 0 and mp.y != 0):
        f.rot = Vector3((0,600/mp.y * pi,600/mp.x * pi))
    f.render(screen)
    pygame.display.update()
    screen.fill((0,0,0))
