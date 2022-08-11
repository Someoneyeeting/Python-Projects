from Vector3 import Vector3
from Matrix import Matrix
from math import *
from pygame import Color,Vector2,draw,mouse,Rect
from copy import deepcopy

class Face:
    points = [Vector3((-1,-1,0)),Vector3((-1,1,0)),Vector3((1,-1,0)),Vector3((1,1,0))]
    rpoints = points[::]
    rot = Vector3((0,0,0))
    color = Color(255,255,255)
    pos = Vector3((10,0,0))
    scale = 100
    def __init__(self) -> None:
        pass
    def render(self,screen):
        for i in range(4):
            while self.rot.x > pi * 2:
                self.rot.x -= pi * 2
            while self.rot.x < pi * 2:
                self.rot.x += pi * 2
            while self.rot.y > pi * 2:
                self.rot.y -= pi * 2
            while self.rot.y < pi * 2:
                self.rot.y += pi * 2
            while self.rot.z > pi * 2:
                self.rot.z -= pi * 2
            while self.rot.z < pi * 2:
                self.rot.z += pi * 2
            self.rpoints[i] = deepcopy(self.points[i])
            self.rpoints[i] = self.rpoints[i].rotateX(self.rot.x)
            self.rpoints[i] = self.rpoints[i].rotateY(self.rot.y)
            self.rpoints[i] = self.rpoints[i].rotateZ(self.rot.z)
            self.rpoints[i] *= self.scale 
            self.rpoints[i] += self.pos
            depth = 1 / ( (0.6 + (self.rpoints[i].z / (1 * 2))))
            depthmat = Matrix([[depth,0,0],[0,depth,0]])
            depthmat = depthmat * self.rpoints[i]
            depthmat = Vector2(depthmat.get(0,0),depthmat.get(1,0))
            # drawposes.append(Vector3((drawpos.x,drawpos.y,i.z)))
            self.rpoints[i] = Vector3((self.rpoints[i].x,self.rpoints[i].y,self.rpoints[i]))
        for i in range(2):
            p = self.rpoints[i]
            pn = self.rpoints[(i + 1)% 4]
            pnn = self.rpoints[(i + 2)% 4]
            depth = p.z + pn.z + pnn.z
            depth /= 3
            draw.polygon(screen,(self.color),[p.get2D(),pn.get2D(),pnn.get2D()])
