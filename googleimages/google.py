# importing google_images_download module
from re import search
from google_images_download import google_images_download 
import os,shutil,pyimgur,keyboard,mouse,webbrowser,time
from PIL import Image

response = google_images_download.googleimagesdownload() 
  
  

def downloadimages():
    suffix = " mugshot"
    search_queries = [
    'phoenix wright',
    "miles edgeworth",
    "manfred von karma",
    "apollo justice",
    "athena cykes",
    "maya fey",
    "mia fey",
    "godot ace attorney",
    "franziska von karma",
    "klavier gavin",
    "simon blackquil",
    "larry butz",
    "dahlia hawthorne",
    "kristoph gavin",
    "detective gumshoe",
    "kristoph gavin",
    "judge ace attorney",
    "Quercus Alba",
    "bobby fullbright",
    "damon gant",
    "jake marshall",
    "redd white",
    "luke atmey",
    "herlock sholmes",
    "richard wellington",
    "autopsy report ace attorney",
    "hobo phoenix wright",
    "wendy oldbag",
    "winston payne",
    "sebestian debeste",
    "shelly de killer",
    "maximillion galactica",
    "ron deLite",
    "raymond sheilds",
    "khurain judge"
    ]
    for i in search_queries:
        arguments = {"keywords": i + suffix,
                    "limit":10}
        response.download(arguments)
    suffix = " head"
    search_queries = [
        "kris",
        "susie",
        "ralsie",
        "sans",
        "noelle",
        "spamton",
        "berdly",
        "light yagami",
        "L death note",
        "ryuk",
        "saitma",
        "DIO",
        "jotaro",
        "queen deltarune",
        "ness earthbound",
        "paula earthbound",
        "jeff earthbound",
        "giorno giovanna",
        "enrico pucci",
        "jolyne",
        "diavolo",
        "doppio",
        "yoda",
        "master oogway"
    ]
    
    for i in search_queries:
        arguments = {"keywords": i + suffix,
                    "limit":10}
        response.download(arguments)


def copy():
    for i in os.listdir("./downloads"):
        path = "./downloads/" + i + "/"
        shutil.copyfile(path + os.listdir(path)[0],"./selected/" + i.replace(" mugshot","").replace(" head","").replace(" ace attorney","") + ".png")

def topng():
    for i in os.listdir("./selected"):
        img = Image.open("./selected/" + i)
        img.save("./selected/" + i) 

def upload():
    id = "bf7162304002178"
    secret = "183bb038e74e10c9d7dcb0dba89ed5567895c193"
    im = pyimgur.Imgur(id)
    with open("uploads.txt","w") as f:
        for i in os.listdir("./selected"):
            print("E:/python/googleimages/selected/" + i)
            image = im.upload_image("E:/python/googleimages/selected/" + i,title = i.replace(".png",""))
            f.write(i.replace(".png","") + ": " + image.link + "\n")
        f.close()
def fill():
    with open("uploads.txt","r") as f:
        data = f.read()
        data = data.split("\n")
        data = [i.split(": ") for i in data]
        for i in data:
            print(i)
            keyboard.wait("ctrl+shift")
            mouse.click()
            keyboard.write(i[0])
            keyboard.wait("ctrl+shift")
            mouse.click()
            keyboard.write(i[1])

            
def check():
    while True:
        if(keyboard.is_pressed("q")):
            print(mouse.get_position())
            
fill()
