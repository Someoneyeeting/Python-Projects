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

def shufflej():
    global dect
    with open("en_us.lang") as f:
        dect = json.load(f)

    keys = settolist(dect.keys())
    values = settolist(dect.values())
    forbiden = "language.name English language.region United States language.code en_us"
    for i in range(40000):
        x = randrange(0, len(values))
        y = randrange(0, len(values))
        if(x in forbiden or y in forbiden):
            continue
        z = deepcopy(values[y])
        values[y] = deepcopy(values[x])
        values[x] = deepcopy(z)

    final_dict = {}
    for i in range(len(keys)):
        final_dict[keys[i]] = values[i]

    with open("lang/en_us.json","w") as f:
        json.dump(final_dict,f)
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
    filenames = next(walk(dira), (None, None, []))[1]
    # print("dirs: {filenames}")
    for i in filenames:
        searchdira(dira + "/" + i)

searchdira("textures")

def replace(f1,f2):
    print(f1,f2,"\n")
    try:
        os.rename(f1,f1 + "c")
        os.rename(f2,f1)
        os.rename(f1 + "c",f2)
    except:
        pass

def shuffle():
    for i in files:
        for x in files[i]:
            replace(x[1],files[i][randrange(len(files[i]))][1])


searchdira("textures")
shuffle()

input("done")