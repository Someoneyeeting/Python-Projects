from ctypes import windll
import pyautogui,time,mouse,keyboard,random
from PIL import ImageGrab

#(681, 582)
off = 520 / 7,450 / 6

def first_empty(col,board):
    for i in range(6)[::-1]:
        if board[col][i] == 0:
            return i
    return -1
def randomagent(board):
    return random.randrange(0,7)
def checkhor(board,pos,player):
    places = []
    for j in range(4):
        piece = 0
        for i in range(4):
            if(pos[0] + i - j  not in range(7)):
                continue
            if(board[pos[0] + i - j][pos[1]] == player):
                piece += 1
                continue
            if board[pos[0] + i - j][pos[1]] != 0:
                piece = 0
                break
        
        places.append(piece)
    return max(places)
def checkver(board,pos,player):
    places = []
    for j in range(4):
        piece = 0
        for i in range(4):
            if(pos[1] + i - j  not in range(6)):
                break
            if(board[pos[0]][pos[1] + i - j] == player):
                piece += 1
                continue
            if board[pos[0]][pos[1] + i - j] != 0:
                piece = 0
                break
        
        places.append(piece)
    return max(places)
def checkldia(board,pos,player):
    places = []
    for j in range(4):
        piece = 0
        for i in range(4):
            if(pos[0] + i - j not in range(7) or pos[1] + i - j  not in range(6)):
                break
            if(board[pos[0] + i - j][pos[1] + i - j] == player):
                piece += 1
                continue
            if board[pos[0] + i - j][pos[1] + i - j] != 0:
                piece = 0
                break
        
        places.append(piece)
    return max(places)
def checkrdia(board,pos,player):
    for i in board:

        places = []
        for j in range(4):
            piece = 0
            for i in range(4):
                if(pos[0] + (3 - i) - (3 - j) not in range(7) or pos[1] + i - j not in range(6)):
                    break
                if(board[pos[0] + (3 - i) - (3 - j)][pos[1] + i - j] == player):
                    piece += 1
                    continue
                if board[pos[0] + (3 - i) - (3 - j)][pos[1] + i - j] != 0:
                    piece = 0
                    break
            places.append(piece)
        return max(places)
def check(board,pos,player):
    m = [checkver(board,pos,player),checkhor(board,pos,player),checkldia(board,pos,player),checkrdia(board,pos,player)]
    if(max(m) == 4): return 100000
    score = 0
    for i in m:
        if i == 3: score += 1
    
    return score
    

board = [[0 for i in range(6)] for i in range(7)] 
lastboard = [i.copy() for i in board]


player = 0
def play(player):
    print(player)
    image = ImageGrab.grab().load()
    for y in range(6):
        for x in range(7):
            px,py = 453 + (x * off[0]),204 + (y * off[1])
            pix = image[mouse.get_position()]
            board[x][y] = 1 if image[px,py][2] == 0 else 2 if image[px,py][0] == 0 else 0
    if(keyboard.is_pressed("s")):
        exit()
    plays = []
    for i in range(7):
        b = [i.copy() for i in board]
        emp = first_empty(i,b)
        if(b[i][5] != 0):
            plays.append(-1)
            continue
        b[i][emp] = player
        score = check(b,(i,emp),player)
        b[i][emp] = 1 if player == 2 else 2
        score = max(check(b,(i,emp),1 if player == 2 else 2),score)
        plays.append(score)
            
    m,mdx = min(plays),random.randrange(7)
    for i in range(len(plays)):
        if(plays[i] > m):
            m = plays[i]
            mdx = i

    mouse.move(453 + (mdx * off[0]),204)
    mouse.click()
    time.sleep(0.5)

keyboard.add_hotkey("q",play,args=[1])
keyboard.add_hotkey("e",play,args=[2])

while True:
    keyboard.read_key()
