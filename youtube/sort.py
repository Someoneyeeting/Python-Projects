comments = []

with open("potatocomment.txt","r",encoding="utf-8") as f:
    comments = f.read()
    f.close()
    
comments = comments.split("\n\n")

commentslist = []
likes = []
for idx,i in enumerate(comments):
    comments[idx] = i.split(" ")
    try:
        likes.append(int(comments[idx][0]))
    except:
        pass

likes.sort()

print(likes)