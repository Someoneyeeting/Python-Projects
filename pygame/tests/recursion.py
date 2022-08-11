import sys,pygame,keyboard
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
import copy

from pygame import mouse
from pygame.event import wait

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600

screen = pygame.display.set_mode(size)

def rect(pos,w):
    if pos.distance_squared_to(Vector2(300,300)) > 100 ** 2:
        return
    draw.rect(screen,Color(255,255,255),Rect(pos - Vector2(w / 2,w / 2),Vector2(w,w)))
    nw = w / 1
    rect(Vector2(pos.x - nw,pos.y),nw)
    rect(Vector2(pos.x + nw,pos.y),nw)
    rect(Vector2(pos.x,pos.y - nw),nw)
    rect(Vector2(pos.x,pos.y + nw),nw)

rect(Vector2(300,300),100)
while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.update()
