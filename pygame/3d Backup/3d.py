import math
import sys,pygame
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
import copy
from Matrix import Matrix
from Vector3 import Vector3

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600

def connect(p1,p2,l):
    pos1 = l[p1]
    pos2 = l[p2]
    draw.line(screen,Color(255,255,255),pos1.get2D(),pos2.get2D())

points = [(-1,-1,1),
          (1,-1,1),
          (1,1,1),
          (-1,1,1),
          (-1,-1,-1),
          (1,-1,-1),
          (1,1,-1),
          (-1,1,-1),]

points = [Vector3(i) for i in points]

cubesize = 50



screen = pygame.display.set_mode(size)

t = 0



while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    t += deltatime
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    mp = Vector2(mouse.get_pos())
    ang = Vector2(0,0)
    ang.x = mp.x / width
    ang.y = mp.y / height
    ang *= pi * 2
    
    drawposes = []
    for i in points:
        i = copy.deepcopy(i)
        i *= cubesize / 2
        i = i.rotateY(-ang.x)
        i = i.rotateX(ang.y)
        # i = i.rotateZ((t / 10) / 180 * pi)
        depth = 1 / ( (0.6 + (i.z / (cubesize * 2))))
        depthmat = Matrix([[2,0,0],[0,2,0]])
        depthmat = Matrix([[depth,0,0],[0,depth,0]])
        depthmat = depthmat * i
        drawpos = Vector2(depthmat.get(0,0),depthmat.get(1,0))
        drawpos += Vector2(width/2,height/2)
        drawposes.append(Vector3((drawpos.x,drawpos.y,i.z)))
        # draw.circle(screen,Color(255,255,255),drawpos,3 * depth)
        
        
   
    for i in range(4):
        connect(i,(i + 1) % 4,drawposes)
        connect(i + 4,((i+1) % 4) + 4,drawposes)
        connect(i,i+4,drawposes)
    
    
   
    pygame.display.update()
    screen.fill((0,0,0))
