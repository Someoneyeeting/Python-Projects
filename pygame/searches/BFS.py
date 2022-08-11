import queue
import sys,pygame,keyboard
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
import copy

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600

screen = pygame.display.set_mode(size)

gridsize = 16
scale = 600/gridsize

grid = [[0 if i != 8 else 15 for i in range(gridsize)] for i in range(gridsize)]

def getnighbors(pos):
    offs = [(1,0),(-1,0),(0,1),(0,-1)]
    poses = []
    for i in offs:
        if(pos[0] + i[0] >= 0 and pos[0] + i[0] < gridsize and pos[1] + i[1] >= 0 and pos[1] + i[1] < gridsize):
            poses.append((pos[0] + i[0],pos[1] + i[1]))
    return poses

def bfs(grid,v):
    queue = [v]
    visited = 0
    startval = grid[v[0]][v[1]]
    while len(queue) > 0:
        v = queue.pop(0)
        if(grid[v[0]][v[1]] == startval):
            grid[v[0]][v[1]] = 15 - grid[v[0]][v[1]]
            nigh = getnighbors(v)
            for i in nigh:
                if(i not in queue and grid[i[0]][i[1]] == startval):
                    queue.append(i)

a = 0
dir = 1
while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    mp = mouse.get_pos()
    gridmp = (int((mp[0] / 600) * gridsize),int((mp[1] / 600) * gridsize))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                bfs(grid,gridmp)
    if(mouse.get_pressed()[0]):
        grid[gridmp[0]][gridmp[1]] = 15
    elif(mouse.get_pressed()[2]):
        grid[gridmp[0]][gridmp[1]] = 0
    # grid = [[0 for i in range(gridsize)] for i in range(gridsize)]
    # gridmp = (int(mp[0] / 600 * gridsize),int(mp[1] / 600 * gridsize))
    # bfs(grid,gridmp) 
    
    for y in range(gridsize):
        for x in range(gridsize):
            clr = int((grid[x][y] / (gridsize)) * 255)
            try:
                draw.rect(screen,Color(clr,clr,clr),Rect(x * scale,y * scale,scale * 1.3,scale * 1.3))
            except:
                print(clr)
    pygame.display.update()
    screen.fill((0,0,0))
