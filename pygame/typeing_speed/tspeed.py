import sys,pygame,keyboard,copy,msvcrt
from pygame import Color,Vector2,draw,mouse,Rect
from math import *
from random import *

from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600

words = ["python","java","c++","coding","programming","minecraft","idk","jevil"]

wordsobj = []

myfont = pygame.font.SysFont('Comic Sans MS', 30)

class Word:
    global words,wordsobj,screen
    def __init__(self) -> None:
        self.pos = Vector2(-100,randrange(50,550))
        self.word = words[randrange(len(words))]
        self.typed = 0
        self.totype = self.word[0]
        wordsobj.append(self)

    def update(self):
        self.totype = self.word[self.typed]
        if(self.typed == len(self.word) - 1):
            wordsobj.remove(self)
            del self
        screen.
    def check(self):
        if(keyboard.is_pressed(self.totype)):
            self.typed += 1
        else:
            self.typed = 0

pressed = []

def delk(dic,k):
    x = dic
    del x[k]
    return x

screen = pygame.display.set_mode(size)

wpm = 20
spawntime = 0

while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    checked = False
    spawntime += deltatime
    todel = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if(event.type == pygame.KEYDOWN):
            if not checked:
                for i in wordsobj:
                    i.check()
                checked = True
    pygame.display.update()
    screen.fill((0,0,0))
