import sys,pygame,keyboard
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *
import copy
from tkinter import *
from tkinter import messagebox

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 635,477

icon = pygame.image.load("./icon.png")

img = pygame.image.load("./OneTail.png")
imgrect = img.get_rect()
screen = pygame.display.set_mode(size)

pygame.display.set_icon(icon)
pygame.display.set_caption("OneTail")


while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Tk().wm_withdraw()
            messagebox.showinfo("stay?","are you sure you want to continue?")

    screen.blit(img,imgrect)
    pygame.display.update()
    screen.fill((0,0,0))
