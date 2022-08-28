from PIL import Image
import math,random


image = Image.open("img.jpg")

def length(x,y):
    return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2 + (y[1] - x[1]) ** 2)

def inttup(x):
    return (int(x[0]),int(x[1]),int(x[2]))

img = image.load()
size = image.size

def getnighbors(pos):
    offs = [(1,0),(-1,0),(0,1),(0,-1)]
    poses = []
    for i in offs:
        if(pos[0] + i[0] >= 0 and pos[0] + i[0] < size[0] and pos[1] + i[1] >= 0 and pos[1] + i[1] < size[1]):
            poses.append((pos[0] + i[0],pos[1] + i[1]))
    return poses

def bfs(grid,v):
    queue = [v]
    visited = 0
    startval = grid[v[0],v[1]]
    while len(queue) > 0:
        v = queue.pop(0)
        if(length(grid[v[0],v[1]],startval) < 50):
            nigh = getnighbors(v)
            for i in nigh:
                if(i not in queue and length(grid[v[0],v[1]],startval) < 50):
                    queue.append(i)
                    visited += 1
    return visited


blur = 5
for y in range(size[1]):
    for x in range(size[0]):
        pix = img[x,y]
        g = bfs(img,(x,y))
        img[x,y] = g
image.show()
image.save("done.png")