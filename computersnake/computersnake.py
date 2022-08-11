from logging import root
from tkinter import *
import time

win = Tk()
win.title("snake")

def openWindow():
    global win
    window = Toplevel(win)
    window.title("snake")
    win = window


for i in range(5):
    print("hello")
    openWindow()
    time.sleep(1)