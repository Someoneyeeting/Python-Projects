import keyboard
from pyfirmata import Arduino,util
import time

board = Arduino("COM3")

it = util.Iterator(board)
it.start()

p8 = board.get_pin("d:3:o")

p8.write(1)

# global power
# power = 0

# def func():
#     global power
#     power = 0 if power == 1 else 1
#     keyboard.press_and_release("backspace")
#     print(power)

# keyboard.add_hotkey("q",func)

# while not keyboard.is_pressed("g"):
#     p8.write(1)
# else:
#     keyboard.press_and_release("backspace")

board.exit()