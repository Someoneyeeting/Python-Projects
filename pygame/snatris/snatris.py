import sys,pygame
from pygame import Color,Vector2,draw,mouse
from math import *
from random import *
import copy

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

gridsize = Vector2(50,50)

tiles = [[0] * int(gridsize.x)] * int(gridsize.y)
mtiles = []
size = width,height = 600,600


class Tile:
    pos,color,moving = 0,0,True
    def __init__(self,pos,color) -> None:
        self.pos = pos
        self.color = color
    def update(self):
        tiles[self.pos.x][self.pos.y] = [0]
        if(self.moving):
            if(self not in mtiles):
                mtiles.append(self)
            self.pos += 1
        else:
            if(self in mtiles):
                mtiles.remove(self)
        tiles[self.pos.x][self.pos.y] = self
        print("update")
    def draw(self):
        draw.rect(screen,self.color,pygame.Rect(self.pos * gridsize,Vector2(size) / gridsize))
        
til = Tile(Vector2(25,0),Color(100,63,255))
tiles.append(til)

def tick():
    for i in tiles:
        if i is Tile:
            i.update()
    print("tick")


screen = pygame.display.set_mode(size)

time = 0
while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    time += deltatime
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if(time >= 1):
        tick()
        time = 0
    for i in tiles:
        if(i is Tile):
            i.draw()
    pygame.display.update()
    screen.fill((0,0,0))
