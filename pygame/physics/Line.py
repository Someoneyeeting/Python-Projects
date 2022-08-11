from pygame.draw import line
from pygame import Color,Vector2
class Line:
    p1,p2,s,c = 0,0,0,0
    def __init__(self,po1 ,po2) -> None:
        self._p1 = po1
        self._p2 = po2
        self.p1 = self.p1
        self.p2 = self.p2()
        self.setvars()
    
    def draw(self,screen):
        line(screen,Color(255,255,255),self.p1,self.p2,2)
    
    def intersect(self,line):
        if(line.s == self.s):
            return None

        point = Vector2(0,0)
        point.x = (self.c - line.c) / -(self.s - line.s) 
        point.y = (self.s * point.x) + self.c
        if(point.x > min(self.p1.x,self.p2.x) and point.x < max(self.p1.x,self.p2.x) and point.x > min(line.p1.x,line.p2.x) and point.x < max(line.p1.x,line.p2.x)):
            return point
        return None
    @property
    def p1(self):
        return self._p1
    @property
    def p2(self):
        return self._p2
    @p1.setter
    def p1(self,v):
        v.x += 0.1 if v.x == self.p2.x else 0
        self._p1 = v
        self.setvars()
    
    @p2.setter
    def p2(self,v):
        v.x += 0.1 if v.x == self.p1.x else 0
        self._p2 = v
        self.setvars()
        
    def setvars(self):
        self.s = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        self.c = self.p2.y - (self.s * self.p2.x)