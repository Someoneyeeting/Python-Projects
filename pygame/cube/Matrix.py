from typing import List, Tuple
from copy import deepcopy
import sys
from math import *


class Matrix:
    mat = []
    size = (0,0)
    def __init__(self,mat):
        from Vector3 import Vector3
        if isinstance(mat,list):
            self.mat = mat
            for i in range(len(self.mat)):
                if(i == 0) : continue
                if (len(self.mat[i]) != len(self.mat[i - 1])):
                    raise("ERROR: cols not equal")
                self.size = (len(self.mat),len(self.mat[0]))
        if isinstance(mat,Vector3):
            self.mat = [[mat.x],[mat.y],[mat.z]]
            self.size = (3,1)

    @staticmethod 
    def zero_mat(size):
        ma = [[0 for i in range(size[1])] for i in range(size[0])]
        ma = Matrix(ma)
        return ma

    
    def get(self,row,col):
        return deepcopy(self.mat[row][col])
    
    def set(self,row,col,val):
        self.mat[row][col] = deepcopy(val)
    
    def print(self):
        print()
        for i in self.mat:
            print(i)
        print()
    def rotateX(self,rot):
        r = Matrix([[1,0,0],
                    [0,cos(rot),-sin(rot)],
                    [0,sin(rot),cos(rot)]])
        return r * self
    def rotateY(self,rot):
        r = Matrix([[cos(rot),0,-sin(rot)],
                    [0,1,0],
                    [sin(rot),0,cos(rot)]])
        return r * self
    def rotateZ(self,rot):
        r = Matrix([[cos(rot),-sin(rot),0],
                    [sin(rot),cos(rot),0],
                   [0,0,1]])
        return r * self
    def __mul__(self,mat2):
        from Vector3 import Vector3
        if(isinstance(mat2,Vector3)):
            mat2 = Matrix(mat2)
        if(self.size[1] != mat2.size[0]):
            raise("multiplication not possible")
        mulsize = (self.size[0],mat2.size[1])
        newmat = Matrix.zero_mat(mulsize)
        for x in range(newmat.size[0]):
            for y in range(newmat.size[1]):
                for z in range(self.size[1]):
                    # print(x,y,z)
                    newmat.set(x,y,newmat.get(x,y) + (self.get(x,z) * mat2.get(z,y)))
        return newmat
                