import pygame
import subprocess
import os
 
#Create a bunch of images using pygame and save them on the disk as PNG files:
pygame.init()
IMGSIZE = 100
displaysurf = pygame.display.set_mode((IMGSIZE, IMGSIZE))
imagelist = []
filenamelist = [0]*5
for i in range(5):
    pygame.draw.rect(displaysurf, (0, 0, 0), pygame.Rect(0, 0, IMGSIZE, IMGSIZE), 0)
    pygame.draw.rect(displaysurf, (255, 255, 255), pygame.Rect(i*20, i*20, 20, 20), 0)
    #Save as PNG images on disk:
    filenamelist[i] = "pic" + str(i) + ".png"
    pygame.image.save(displaysurf, filenamelist[i])
 
#Combine into a GIF using ImageMagick's "convert"-command (called using subprocess.call()):
convertexepath = "C:/Program Files (x86)/ImageMagick-6.8.9-Q16/convert.exe"  # Hardcoded
convertcommand = [convertexepath, "-delay", "10", "-size", str(IMGSIZE) + "x" + str(IMGSIZE)] + filenamelist + ["anim.gif"]
subprocess.call(convertcommand)
 
#Remove the PNG files (if they were meant to be temporary):
for filename in filenamelist:
    os.remove(filename)