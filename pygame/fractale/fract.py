#import pygame and setup it and screen and on space press 
import pygame
import sys
import random
import time
import math


#setup pygame
pygame.init()


#setup screen
screen = pygame.display.set_mode((600,600))


#main loop
while True:
    #setup screen
    screen.fill((0,0,0))
    #setup event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        rect = pygame.Rect(0,0,800/3,800/3)
        rect.center = screen.get_rect().center
        pygame.draw.rect(screen,(255,255,255),rect)
        pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #setup variables
                #update screen
                pygame.display.update()