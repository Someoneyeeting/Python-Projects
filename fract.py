import mouse,keyboard,time,math

start = (706, 49)
"""
while not keyboard.is_pressed("w"):
    if(not pressed):
        if(keyboard.is_pressed("right")):
            mouse.move(1,0,absolute=False)
        if(keyboard.is_pressed("left")):
            mouse.move(-1,0,absolute=False)
        if(keyboard.is_pressed("up")):
            mouse.move(0,-1,absolute=False)
        if(keyboard.is_pressed("down")):
            mouse.move(0,1,absolute=False)
    pressed = keyboard.is_pressed("down") or keyboard.is_pressed("up") or keyboard.is_pressed("left") or keyboard.is_pressed("right")
    if(keyboard.is_pressed("d")):
        print(mouse.get_position())
"""

size = 1
keyboard.wait("q")
def sqfract():
    for x in range(3):
        for y in range(3):
            if(x == y == 1):
                continue
            keyboard.press_and_release("ctrl+v")
            for i in range(x * size):
                time.sleep(0.06)
                keyboard.press_and_release("right")
            for i in range(y * size):
                time.sleep(0.06)
                keyboard.press_and_release("down")
    if(keyboard.is_pressed("w")):
        exit()
    size *= 3

def idkfract():
    keyboard.press_and_release("ctrl+v")
    keyboard.press_and_release("ctrl+v")
    keyboard.press_and_release("down")
    keyboard.press_and_release("down")
    keyboard.press_and_release("ctrl+v")
    keyboard.press_and_release("down")
    keyboard.press_and_release("right")
    keyboard.press_and_release("right")
    keyboard.press_and_release("right")
    keyboard.press_and_release("ctrl+v")
    keyboard.press_and_release("down")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
      

x = 0  
while not keyboard.is_pressed("w"):
    x += 0.005
    if(x > math.pi * 12 * 2):
        x -= 12 * math.pi
    mouse.move(600 + math.cos(x / 6) * 400,400 + math.sin(x/4) * 100)
    mouse.hold()
    # keyboard.press_and_release("esc")
    # mouse.drag(600,600,0,0,True,0.1)
    # keyboard.press_and_release("ctrl+x")
    # time.sleep(0.1)

mouse.release()