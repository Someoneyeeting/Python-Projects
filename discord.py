import mouse
import keyboard
import time
import random
letters = [
    "A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","1","2","3","4","5","6","7","8","9","0"
]
time.sleep(2)
for c in range(50):
    time.sleep(1/20)
    for i in "discord.gg/":
        keyboard.write(i)
    for i in range(0,random.randrange(1,10)):
        keyboard.write(letters[random.randrange(0,len(letters) - 1)])
    keyboard.write("\n")
for i in "discord.gg/vTRaBZx29X":
    keyboard.write(i)
keyboard.write("\n")
        
    