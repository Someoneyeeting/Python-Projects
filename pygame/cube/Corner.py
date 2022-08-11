from Face import *

class Corner:
    size = 50
    face1 = Face()
    face2 = Face()
    face3 = Face()
    face1.scale = size
    face2.scale = size
    face3.scale = size
    face1.pos = Vector3((size*2,0,0))
    face2.pos = Vector3((0,size*2,0))
    face3.pos = Vector3((0,0,size*2))
    face1.color = Color(255,0,0)
    face2.color = Color(0,255,0)
    face3.color = Color(255,255,255)
    pos = Vector3((0,0,0))
    rot = Vector3((0,0,0))

    def render(self,screen):
        self.face1.rot = Vector3((pi/2,0,0)) + self.rot
        self.face2.rot = Vector3((0,pi/2,0)) + self.rot
        self.face3.rot = Vector3((0,0,pi/2)) + self.rot
        self.face1.pos = Vector3((300,300,0)) + self.face1.rot 
        self.face2.pos = Vector3((300,300,0)) + self.face2.rot
        self.face3.pos = Vector3((300,300,0)) + self.face3.rot