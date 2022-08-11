import sys,pygame,keyboard
from pygame import KEYDOWN, Color,Vector2,draw,mouse,Rect
from math import *
from random import *
import copy
from Line import Line
from pygame import mouse

pygame.init()

getTicksLastFrame = 0
deltatime = 0

size = width,height = 600,600
lines = [Line(Vector2(randrange(0,600),randrange(0,600)),Vector2(randrange(0,600),randrange(0,600))) for i in range(10)]
screen = pygame.display.set_mode(size)

mouse.set_visible(False)

fp = False

class Player:
    pos = Vector2(300,300)
    vision = []
    a,ang,rot,rotspeed,speed = 400,360,0,0.01,30
    def __init__(self) -> None:
        for i in range(self.a):
            rot = (float(i) / float(self.a)) * (self.ang / 180 * pi)
            # rot = rot / pi * 360
            self.vision.append(Line(self.pos,self.pos + Vector2(cos(rot) * 100,sin(rot) * 100)))
    def update(self,screen,delta):
        # self.vision = []
        global fp
        
        defr = Vector2(mouse.get_pos()) - Vector2(300,300)
        self.rot += defr.x * self.rotspeed
        mouse.set_pos((300,300))
        
        mind = 400
        
        if(~fp):
            draw.circle(screen,Color(255,255,255),self.pos,10)
        for idx,i in enumerate(self.vision):
            rota = (self.rot - (self.ang / 300 * pi) / 2) + ((float(idx) / float(self.a)) * (self.ang / 180 * pi))
            # rot = rot / pi * 360
            i.p1 = self.pos
            i.p2 = self.pos + Vector2(cos(rota) * 300,sin(rota) * 300)
            dist = 300
            for x in lines:
                p = i.intersect(x)
                if(p != None):
                    if(self.pos.distance_squared_to(p) < self.pos.distance_squared_to(i.p2)):
                        i.p2 = p
                        dist = self.pos.distance_to(i.p2)
                        if(dist < mind):
                            mind = dist
            
            if(~fp):
                i.draw(screen)
            else:
                dist = 300 - dist
                scale = dist
                scale *= ((abs(idx - (self.a/2)) / 300) + 1) 
                rect = Rect(float(idx)/self.a  * 600,(dist),(600 / float(self.a)),scale)
                g = 255 * dist / 300
                g = int(g)
                draw.rect(screen,Color(g,g,g) ,rect)
                
                # draw.line(screen,Color(255,255,255),Vector2(idx/self.a * 600,600),Vector2(idx/self.a * 600,600 - dist),3)
        v = Vector2(0,0)
        if(keyboard.is_pressed("w")):
            v += Vector2(cos(self.rot),sin(self.rot)) * (self.speed * delta)
        elif(keyboard.is_pressed("s")):
            v -= Vector2(cos(self.rot),sin(self.rot)) * (self.speed * delta)
        if(keyboard.is_pressed("a")):
            v -= Vector2(cos(self.rot + pi/2),sin(self.rot + pi/2)) * (self.speed * delta)
        elif(keyboard.is_pressed("d")):
            v += Vector2(cos(self.rot + pi/2),sin(self.rot + pi/2)) * (self.speed * delta)
        v *= 2 if keyboard.is_pressed("shift") else 1
        if(mind > v.length()):
            self.pos += v

player = Player()

while 1:
    t = pygame.time.get_ticks()
    deltatime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_q):
                lines = [Line(Vector2(randrange(0,600),randrange(0,600)),Vector2(randrange(0,600),randrange(0,600))) for i in range(4)]
            elif(event.key == pygame.K_SPACE):
                fp = ~fp
    
    if(~fp):
        for i in lines:
            i.draw(screen)
    
    player.update(screen,deltatime)
    
    pygame.display.update()
    screen.fill((0,0,0))
