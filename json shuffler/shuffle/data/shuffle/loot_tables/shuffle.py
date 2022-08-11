import os
from os import walk
from random import randrange
import json
from copy import deepcopy

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
        if(i.endswith(".json")):
            files[dira].append((i,dira + "/" + i))
    filenames = next(walk(dira), (None, None, []))[1]
    # print("dirs: {filenames}")
    for i in filenames:
        searchdira(dira + "/" + i)

def replace(f1,f2):
    print(f1,f2,"\n")
    try:
        os.rename(f1,f1 + "c")
        os.rename(f2,f1)
        os.rename(f1 + "c",f2)
    except:
        pass

searchdira("./")
allfiles = []
for i in files:
    for x in files[i]:
        allfiles.append(x[1])

def shuffle():
    for i in files:
        for x in files[i]:
            replace(x[1],allfiles[randrange(len(allfiles))])


shuffle()

input("done")