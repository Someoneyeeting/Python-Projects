import sys,pygame,keyboard
from pygame import Color,Vector2,draw,mouse,Rect,Rect
from math import *
from random import *
import copy

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600

screen = pygame.display.set_mode(size)

g = 980

class Bird:
    pos,rect,v = Vector2(0,0),Rect(0,0,20,20),0
    isjumping = False
    def __init__(self) -> None:
        self.pos = Vector2(70,300)
        self.isjumping = False
    
    def update(self,delta):
        if(delta > 1/6):
            return
        
        self.rect.center = self.pos
        self.v += g * delta
        self.pos.y += self.v * delta
        if(self.isjumping != keyboard.is_pressed("w")):
            self.isjumping = keyboard.is_pressed("w")
            print("jump")
            if(self.isjumping):
                self.v = -450
        draw.circle(screen,Color(230,200,0),self.pos,self.rect.w/2)

bird = Bird()

while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    bird.update(deltatime)
    pygame.display.update()
    screen.fill((0,0,0))
