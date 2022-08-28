import os,json
from googleapiclient.discovery import build
# import BeautifulSoup
  
# HTMLFile = open("index.html", "r")
  
# index = HTMLFile.read()
  
# # Creating a BeautifulSoup object and specifying the parser
# S = BeautifulSoup(index, 'lxml')
  
# # Using the select-one method to find the second element from the li tag
# Tag = S.select_one('li:nth-of-type(2)')
  
# # Using the decompose method
# Tag.decompose()
api = ""
with open("tokens.txt","r") as f:
    api = f.read()
    f.close()

comments = []

with open("potato.html",encoding="utf8") as f:
    comments = f.read()
    f.close()

comments = comments.replace("amp;","")
comments = comments.split("</li><li>")

prefix = "<a href=\"http://www.youtube.com/watch?v="

youtube = build("youtube","v3",developerKey=api)

comment = []

idx = 0
for i in comments:
    idx += 1
    ind = i.find(prefix)
    url = ""
    for x in i[ind + len(prefix)::]:
        if(x == "\""):
            break
        url += x
    
    replay = url.find("=")
    replay = replay + 1 if replay != -1 else 0
    request = youtube.comments().list(
            part="snippet,id",
            id=url[replay::]
        )
    response = request.execute()
    try:
        response = response["items"][0]
        comment.append([
            response["snippet"]["likeCount"],
            response["snippet"]["textDisplay"],
            "http://www.youtube.com/watch?v=" + url])
    except Exception as e:
        print(e)
        print(url)
        print(response)
    print(f"{idx} / {len(comments)}")
    
with open("potatocomment.txt","w", encoding="utf-8") as f:
    for i in comment:
        try:
            f.write(f"{i[0]} {i[1]} {i[2]}\n\n")
        except Exception as e:
            print(e)
            print(i)
    

print(f"{len(comment)} / {len(comments)}")
