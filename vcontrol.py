from pynput.keyboard import Key,Controller
import keyboard

keypress = lambda x : print("hello")

while not keyboard.is_pressed("alt"):
    keyboard.hook_key("q",keypress)
    