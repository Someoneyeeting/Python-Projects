import math,sys,pygame,keyboard
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
from copy import deepcopy
from Matrix import Matrix
from Vector3 import Vector3
from Camera import Camera
from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600


def lerp(A,B,C):
    return (C * A) + ((1-C) * B) 

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
points = [(-1,-1,1),
          (1,-1,1),
          (1,1,1),
          (-1,1,1),
          (-1,-1,-1),
          (1,-1,-1),
          (1,1,-1),
          (-1,1,-1),]

points = [Vector3(i) for i in points]

maxdepth = 0

camera = Camera()

res = 30
def connect(p1,p2,l):
    global maxdepth
    pos1 = l[p1]
    pos2 = l[p2]
    position1 = pos1.get2D()
    position2 = pos2.get2D()
    draw.line(screen,Color(255,255,255),position1,position2)


cubesize = 50 



screen = pygame.display.set_mode(size)

t = 0
mouse.set_pos((300,300))


while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    t ++ deltatime
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if(keyboard.is_pressed("up") or keyboard.is_pressed("w")):
        camera.pos.y -= sin(camera.rot.y) * camera.speed
    elif(keyboard.is_pressed("down") or keyboard.is_pressed("s")):
        camera.pos.y += sin(camera.rot.y) * -camera.speed
    if(keyboard.is_pressed("left") or keyboard.is_pressed("a")):
        camera.pos.x -= 0
    elif(keyboard.is_pressed("right") or keyboard.is_pressed("d")):
        camera.pos.x += 100 * deltatime
    mp = Vector2(mouse.get_pos())
    
    mouse.set_pos((300,300))
    
    ang = Vector2(0,0)
    
    for i in range(len(points)):
        points[i] = points[i].rotateX((mp.y - 300) / 1000)
        points[i] = points[i].rotateY((mp.x - 300) / 1000)
    drawposes = []
    for i in points:
        i = deepcopy(i)
        i *= cubesize / 2
        i = i.rotateY(-ang.x)
        i = i.rotateX(ang.y)
        # i = i.rotateZ((t / 10) / 180 * pi)
        depth = 1 / ( (0.6 + (i.z / (cubesize * 2))))
        depthmat = Matrix([[depth,0,0],[0,depth,0]])
        depthmat = depthmat * i
        drawpos = Vector2(depthmat.get(0,0),depthmat.get(1,0))
        drawpos += Vector2(width/2,height/2)
        # drawpos -= pos
        drawposes.append(Vector3((drawpos.x,drawpos.y,depth)))
        # draw.circle(screen,Color(255,255,255),drawpos,3 * depth)
        
        
   
    for i in range(4):
        connect(i,(i + 1) % 4,drawposes)
        connect(i + 4,((i+1) % 4) + 4,drawposes)
        connect(i,i+4,drawposes)
    
    
   
    pygame.display.update()
    screen.fill((0,0,0))
