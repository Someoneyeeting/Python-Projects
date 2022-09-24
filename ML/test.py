import sys
import pygame
from pygame import draw,Color,Vector2,mouse
from random import *
import time
from math import *
from pygame.locals import *
from network import *

pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()



width, height = 600,600
screen = pygame.display.set_mode((width, height))

points = []

amount = 2000

class Point:
  def __init__(self,pos,kind):
    self.pos = pos
    self.kind = kind
  def draw(self,surface,vis = False):
    if not vis:
      draw.circle(surface,Color(255,0,0) if self.kind == 0 else Color(0,255,0),self.pos,3)
    else:
      pred = net.classify([self.pos.x,self.pos.y])
      draw.circle(surface,Color(255,0,0) if pred[0] > pred[1] == 0 else Color(0,255,0),self.pos,1)


for i in range(amount):
  pos = Vector2(randrange(20,580),randrange(20,580))
  kind = 1 if pos.y < (0.00099 * pos.x * pos.x) + (-1 * pos.x) + 500 else 0
  points.append(Point(pos,kind))

networksize = [2,5,3,2]

net = Network(networksize)
dataset = Dataset([[i.pos.x,i.pos.y] for i in points],[[i.kind,1 - i.kind] for i in points])

test = Point(Vector2(0,0),1)

x = 0
line = []

cost = net.networkcost(dataset)

lastframe = 0
# Game loop.
while True:
  x += 1
  screen.fill((0, 0, 0))
  print(1 / (time.time() - lastframe))
  lastframe = time.time()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  for i in points:
    i.draw(screen)

  
  
  # print(cost)

  # draw.circle(screen,Color(255,255,255),Vector2(x,300 + sigmoid(((x - 300)) / 100) * 100),4)
  
  test.pos = Vector2(mouse.get_pos())
  pred = net.classify([test.pos.x,test.pos.y])
  test.kind = 1 if pred[0] > pred[1] else 0
  test.draw(screen)

  pygame.display.flip()
  fpsClock.tick(fps)\
  