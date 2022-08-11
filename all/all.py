import os

allfiles = []

def searchdir(dir):
    files = os.listdir(dir)
    for i in files:
        if(i.endswith(".py")):
            allfiles.append(i)
        elif(not ("." in i)):
            try:
                searchdir(dir + "/" + i)
            except:
                pass
            
searchdir("../")
with open("all.txt","w") as f:
    print(len(allfiles))
    for i in allfiles:
        f.write(i + "\n")