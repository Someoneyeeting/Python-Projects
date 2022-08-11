import sys,pygame,keyboard,copy
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
from PIL import ImageGrab
from pygame import mouse
import mouse as mo

pygame.init()


#(453, 204)
#(909, 584)


getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600

screen = pygame.display.set_mode(size)
radius = (600 / 7) / 2

def first_empty(col):
    for i in range(6)[::-1]:
        if board[col][i] == 0:
            return i
    return -1

player = True
playing = True


def check_ver(x,y):
    p = board[x][y]
    for i in range(4):
        if(board[x - i][y] != p):
            print(x - i)
            return False
    return True

def check_win(x,y):
    for i in range(4):
        win = check_ver(x - i,y)
        if(win):
            return True
    return False

def play(col):
    global player,playing
    print(col)
    emp = first_empty(col)
    if(emp == -1):
        return
    player = not player
    board[col][emp] = 1 if player else 2
    win = check_win(col,emp)
    if(win):
        print(("Red" if player else "Blue") + " Win")
        playing = False

handled = False
while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and playing:
            pos = pygame.mouse.get_pos()
            # play(int(pos[0] / (600/7)))
    for y in range(6):
        for x in range(7):
            clr = Color(70,70,70) if board[x][y] == 0 else Color(255,20,20) if board[x][y] == 1 else Color(20,20,255) 
            draw.circle(screen,clr,((x/7 * 600) + radius,(y/6*600) + radius),radius)
    pygame.display.update()
    screen.fill((0,0,120))
