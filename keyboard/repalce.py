import keyboard,pyperclip,time,random

def rep():
    clip = pyperclip.paste()
    keyboard.press_and_release("ctrl+a")
    keyboard.press_and_release("ctrl+c")
    time.sleep(0.01)
    nclip = pyperclip.paste()
    nclip = nclip.split(" ")
    random.shuffle(nclip)
    nclip = " ".join(nclip)
    pyperclip.copy(nclip)
    keyboard.press_and_release("ctrl+v")
    time.sleep(0.06)
    keyboard.press_and_release("enter")
    pyperclip.copy(clip)
    
    
keyboard.add_hotkey("enter",rep,suppress=True)

while True:
    keyboard.read_key()