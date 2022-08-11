from PIL import Image
import os

def checkfolder(path):
    dirs = os.listdir(path)
    for item in dirs:
        dir = path + "//" + item
        try:
            texture = Image.open(dir)
            pixels = texture.load()
            if(not (dir in checked)):
                for x in range(texture.size[0]):
                    for y in range(texture.size[1]):
                        try:
                            r,g,b,a = pixels[x,y]
                            normal = r + g + b
                            normal /= 3 
                            pixels[x,y] = (int(normal),int(normal),int(normal),a)
                        except:
                            try:
                                r,g,b = pixels[x,y]
                                normal = r + g + b
                                normal /= 3 
                                pixels[x,y] = (int(normal),int(normal),int(normal))
                            except:
                                continue
                        
                texture.save(dir)
                checked.append(dir)
        except:
            checkfolder(path + "//" + item) 
                
checked = []

maindir = __file__.replace(r"blacknwhitetextures.py","")
targetpath = input()
checkfolder(targetpath)
print("done")

