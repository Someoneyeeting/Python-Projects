from PIL import Image
import os
from os import walk
from random import randrange
import json
from copy import deepcopy

def settolist(set):
    lis = []
    for i in set:
        lis.append(i)
    return lis 

files = {}


def sep(filename):
    name = ""
    for i in filename[::-1]:
        if i == "/" : break
        name += i
    name = name[::-1]
    return name,filename.replace("/" + name, "")

def getfull(key):
    return key + "/" + files[key]

def settolist(set):
    lis = []
    for i in set:
        lis.append(i)
    return lis
def searchdira(dira):
    if("font" in dira):return
    filenames = next(walk(dira), (None, None, []))[2]
    # print("files: {filenames}")
    files[dira] = []
    for i in filenames:
        if(i.endswith(".png")):
            files[dira].append((i,dira + "/" + i))
            im = dira + "/" + i
            if("wool" not in im and "clay" not in im):
                continue
            print(im)
            with Image.open(im) as img:
                px = img.load()
                s = img.size
                for x in range(s[0]):
                    for y in range(s[1]):
                        try:
                            px[x,y] = (int(255/2),int(255/2),int(255/2))
                        except:
                            print(px[x,y],im)
                            break    
                img.save(im)

    filenames = next(walk(dira), (None, None, []))[1]
    # print("dirs: {filenames}")
    for i in filenames:
        searchdira(dira + "/" + i)

searchdira("textures")


