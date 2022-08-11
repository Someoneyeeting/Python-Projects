from PIL import Image
import os
import random

random.seed(os.times())
mp3s = []
oggs = []
used = []
def checkmp3s(path):
    dirs = os.listdir(path)
    for item in dirs:
        if (".mp3" in item):
            mp3s.append(item)
            
def checkoggs(path):
    dirs = os.listdir(path)
    for item in dirs:
        if (".ogg" in item):
            oggs.append(item)
def findmp3s():
    replacename = mp3s[random.randrange(0,len(mp3s))]
    if replacename in used:
        replacename = findmp3s()
    used.append(replacename)
    return replacename
def findoggs():
    replacename = oggs[random.randrange(0,len(oggs))]
    if replacename in used:
        replacename = findoggs()
    used.append(replacename)
    return replacename
path = "E:\\SteamLibrary\\steamapps\\common\\Geometry Dash\\Resources"

checkmp3s(path)
checkoggs(path)

for music in mp3s:
    os.rename(path + "\\" + music,path + "\\tempreplace" +  findmp3s())
for music in mp3s:
    os.rename(path + "\\tempreplace" + music,path + "\\" + music.replace("tempreplace",""))

for music in oggs:
    os.rename(path + "\\" + music,path + "\\tempreplace" +  findoggs())
for music in oggs:
    os.rename(path + "\\tempreplace" + music,path + "\\" + music.replace("tempreplace",""))
