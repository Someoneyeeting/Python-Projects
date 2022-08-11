import win32gui
import win32api
import random

dc = win32gui.GetDC(0)
print(win32gui.GetPixel(0,0))