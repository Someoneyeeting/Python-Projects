from ast import keyword
import keyboard
import pyperclip
import time
import numpy
import mouse
import os,sys

pyperclip.copy(" ")
board = []

restartpos = (807, 464)
startpos = (686, 283)


def readfile():
    with open("board.txt","r") as f:
        for i in f.read().split("\n"):
            row = []
            for x in i.split(" "):
                row.append(int(x))
            board.append(row)
        f.close()
    
def readboard():
    row = ""
    for i in range(81):
        if(keyboard.is_pressed("e")):
            exit()
        keyboard.press_and_release("ctrl+a")
        keyboard.press_and_release("backspace")
        keyboard.press_and_release("ctrl+c")
        time.sleep(0.04) 
        row += pyperclip.paste()
        pyperclip.copy(" ")
        if((i + 1)%9 == 0 or i == 80):
            keyboard.press_and_release("down")
            board.append([int(i) if i != " " else -1 for i in row])
            row = ""
        keyboard.press_and_release("right")

def getcell(x,y):
    global board
    return(board[y][x])

def setcell(x,y,v):
    global board
    board[y][x] = v

def possible(x,y,n):
    for i in range(9):
        if(i != y and getcell(x,i) == n):
            return False
        if(i != x and getcell(i,y) == n):
            return False
    x0,y0 = x//3 * 3,y//3 * 3
    for i in range(3):
        for j in range(3):
            if(x0 + i != x and y0 + j != y):
                if(getcell(x0 + i,y0 + j) == n):
                    return False
    return True



def done():
    for i in board:
        for x in i:
            if(x == -1):
                return False
    return True

def solve():
    for i in range(81):
        if(keyboard.is_pressed("e")):
            exit()
        keyboard.press_and_release("ctrl+a")
        x,y = i % 9,i//9
        if(getcell(x,y) != -1):
            keyboard.press_and_release(str(getcell(x,y)))
        keyboard.press_and_release("right")
        time.sleep(0.04)
        if((i + 1)%9 == 0 or i == 80):
            keyboard.press_and_release("down")
    keyboard.press_and_release("enter")


# with open("board.txt","w") as f:
#     for i in board:
#         for x in i:
#             f.write(str(x) + " ")
#         f.write("\n")
# readfile()

def sol(depth = 0):
    for y in range(9):
        for x in range(9):
            if(getcell(x,y) == -1):
                for i in range(1,10):
                    if possible(x,y,i):
                        setcell(x,y,i)
                        if(not sol()):
                            setcell(x,y,-1)
                        else:
                            return True
                return False
    
    solve()
    return True
                        
keyboard.wait("q")

while not keyboard.is_pressed("e"):
    time.sleep(1.3)
    mouse.move(restartpos[0],restartpos[1])
    mouse.click()
    mouse.move(startpos[0],startpos[1])
    time.sleep(1.4)
    mouse.click()
    board = []
    readboard()
    sol()
#     readboard()
#     tocheck = []
    
#     for x in range(9):
#         for y in range(9):
#             if(getcell(x,y) == -1):
#                 tocheck.append((x,y))
#     sol()
        
#     # solve()
#     print(numpy.matrix(board))
#     break
