import sys,pygame,copy,keyboard
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *

from pygame import mouse

pygame.init()

colors = [Color(0,0,0),Color(255,0,0),Color(0,255,0),Color(0,0,255),Color(255,255,0),Color(255,0,255),Color(0,255,255),Color(100,100,255),Color(255,255,255)]

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600
ccount = 30
csize = width/ccount
ticktime = 40

cells = [x == 14 for x in range(ccount) for y in range(ccount)]
nc = copy.deepcopy(cells)
clock = pygame.time.Clock()


def getcell(x,y,cell = cells):
    # try:
    return cell[(x % ccount) + ((y - 1) * ccount)]
    # except:
    #     print(x,y)
def setcell(x,y,c,cell = cells):
    cell[(x % ccount) + ((y - 1) * ccount)] = c
def postonum(x,y):
    return (x % ccount) + (y * ccount)
def getaround(x,y,cell = cells):
    alive = 0
    for xx in [-1,0,1]:
        for yy in [-1,0,1]:
            if(xx == 0 and yy == 0):
                continue
            # print(xx,yy)
            if(getcell(x + xx,y + yy,cell)):
                alive += 1
                # draw.rect(screen,Color(0,255,0),Rect(((x + xx) * csize) - 3,((y + yy) * csize) - 3,csize + 6,csize + 6))
    return alive

screen = pygame.display.set_mode(size)
z = 0
t = 0
playing = False
while 1:
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing
                t = 0
                
    mx,my = mouse.get_pos()
    mcx,mcy = int(mx / csize),int(my / csize)
    if(mouse.get_pressed()[0]):
        setcell(mcx,mcy,True,cells)
    elif(mouse.get_pressed()[2]):
        setcell(mcx,mcy,False,cells)
    # cells[z] = not cells[z]
    # z -= 1
    # z = z % (ccount * ccount)
    
    if(playing):
        if(t > ticktime):
            nc = cells[::]
            for x in range(ccount):
                for y in range(ccount):
                    around = getaround(x,y,nc)
                    alive = False
                    if(getcell(x,y,cells)):
                        alive = around == 2 or around == 3
                    else:
                        alive = around == 3
                    setcell(x,y,alive)
            t = 0
        else:
            t += 1            
    
    # print(cells == nc)
    for x in range(ccount):
        for y in range(ccount):
            if(getcell(x,y,cells)):
                draw.rect(screen,Color(255,255,255),Rect(x * csize,y * csize,csize,csize))
    
    pygame.display.update()
    screen.fill((0,0,0))
