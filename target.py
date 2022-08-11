#initalize pygame and screen 600x600
import pygame
from pygame.locals import *
from pygame import Vector2
import sys
import time
import random
import math
from copy import deepcopy


pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Copilot")

#class Bullet with a Vector2 pos, Vector2 vel, and a red rectangle and a update and a draw method
class Bullet:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 5, 5)
        self.rect.center = self.pos.x, self.pos.y
        self.color = (random.randrange(255),random.randrange(255),random.randrange(255))
        #unchanged varable init_vel
        self.init_vel = deepcopy(vel)

    def calcMaxHeight(self):
        #calculate max height
        return (self.init_vel.y**2 / (2 * 9.8))

    def CalcFlightTime(self):
        #calculate flight time
        return (self.init_vel.y / 0.98) * 2

    def travel(self):
        #calculate distance traveled
        return -(self.init_vel.x * self.CalcFlightTime())

    def update(self):
        #gravity of 9.8
        if(self.pos.y + self.vel.y > 500):
            self.vel = Vector2(0,0)
            self.pos = Vector2((self.travel() + 100) % 600, 500)
        else:
            self.vel.y += 0.98
        self.pos.x %= 600
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.rect.center = self.pos.x, self.pos.y
        

    def draw(self):
        # pygame.draw.circle(screen, self.color, Vector2((self.travel() + 100) % 600,500), 5)
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.line(screen, self.color, self.rect.center,
                         Vector2((self.travel() + 100) % 600, 500))


#list of bullets
bullets = []

def spawn():
    mouse_pos = pygame.mouse.get_pos()
    #angle from 100,500 to mouse
    angle = math.atan2(mouse_pos[1] - 500, mouse_pos[0] - 100)
    #max height is the distance from the mouse to y = 500
    max_height = abs(mouse_pos[1] - 500)
    #angle to Vector2
    vel = Vector2(math.cos(angle), math.sin(angle))
    #v.y * magnitude == sqrt(1.96 * max_hieght)
    vel.y *= math.sqrt(1.96 * max_height)
    vel.x = (100 - mouse_pos[0]) * 2 / ((vel.y / 0.98))
    #create bullet
    bullets.append(Bullet(Vector2(100,500), vel))


#main loop
while True:
    #get user input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        #onclick
        elif event.type == MOUSEBUTTONDOWN:
            spawn()
        #on click summon a bullet at 100,500 with a velocity of angel towards the mouse and magnitude of 20
    #update the screen
    screen.fill((0,0,0))
    #delete the oldest bullet if the list is bigger than 5
    if(len(bullets) > 60):
        bullets.pop(0)
    #draw a ground as a green line 
    pygame.draw.line(screen, (0,255,0), (0,500), (600,500))
    #update the bullets
    for bullet in bullets:
        bullet.update()
        bullet.draw()
    pygame.display.update()
    #wait a little bit
    time.sleep(0.005)
