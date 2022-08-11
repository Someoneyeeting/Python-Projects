from typing import Tuple,TYPE_CHECKING
from math import *
import sys

from pygame import Vector2

class Vector3:
    x = y = z = 0
    def __init__(self,pos):
        from Matrix import Matrix
        if isinstance(pos,Tuple):
            self.x = pos[0]
            self.y = pos[1]
            self.z = pos[2]
        elif isinstance(pos,Matrix):
            self.x = pos.get(0,0)
            self.y = pos.get(1,0)
            self.z = pos.get(2,0)
    
    def print(self):
        print("[" + str(self.x),str(self.y),str(self.z) + "]")
        
    def length_squared(self):
        return (self.x ** 2) + (self.y ** 2) + (self.z ** 2)
    def length(self):
        return sqrt(self.length_squared())
    
    def normalized(self):
        len = self.length()
        return self/len
    
    def ang(self):
        return degrees(atan2(self.y,self.x)), degrees(atan2(self.z,self.x))
    
    def ang_to(self,point):
        return degrees(atan2(self.y - point.y,self.x - point.x)),degrees(atan2(self.z - point.z,self.x - point.x))
    
    def rotateX(self,rot):
        from Matrix import Matrix
        r = Matrix([[1,0,0],
                    [0,cos(rot),-sin(rot)],
                    [0,sin(rot),cos(rot)]])
        return Vector3(r * self)
    def rotateY(self,rot):
        from Matrix import Matrix
        r = Matrix([[cos(rot),0,-sin(rot)],
                    [0,1,0],
                    [sin(rot),0,cos(rot)]])
        return Vector3(r * self)
    def rotateZ(self,rot):
        from Matrix import Matrix
        r = Matrix([[cos(rot),-sin(rot),0],
                    [sin(rot),cos(rot),0],
                   [0,0,1]])
        return Vector3(r * self)
    
    def get2D(self):
        return Vector2(self.x,self.y)
    # def rotate(self,ang):
    #     an = self.ang()
    #     len = self.length()
    #     return (Vector3((cos(an[0] + ang[0]) * len),(sin(an[0] + ang[0]) * len))
        
    
    def __add__(self,x):
        return Vector3((self.x + x.x,self.y + x.y,self.z + x.z))
    def __sub__(self,x):
        return Vector3((self.x - x.x,self.y - x.y,self.z - x.z))
    def __mul__(self,x):
        from Matrix import Matrix
        if(isinstance(x,int) or isinstance(x,float)):
            return Vector3((self.x * x,self.y * x, self.z * x))
        elif(isinstance(x,Vector3)):
            return Vector3((self.x * x.x, self.y * x.y, self.z * x.z))
        elif(isinstance(x,Matrix)):
            ma = Matrix(self)
            return ma * x
    def __truediv__(self, x):
        if(isinstance(x,int) or isinstance(x,float)):
            return Vector3((self.x / x,self.y / x, self.z / x))
        elif(isinstance(x,Vector3)):
            return Vector3((self.x / x.x, self.y / x.y, self.z / x.z))
    def __floordiv__(self, x):
        if(isinstance(x,int) or isinstance(x,float)):
            return Vector3((self.x // x,self.y // x, self.z // x))
        elif(isinstance(x,Vector3)):
            return Vector3((self.x // x.x, self.y // x.y, self.z // x.z))
        
        
        