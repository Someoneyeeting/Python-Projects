import serial
import time
import mouse
import keyboard
import math

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

mid = (657, 767)
prevang = 0

def getang(p1,p2):
    return math.atan2(p2[1] - p1[1],p2[0] - p1[0])

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data




while True:
    ang = getang(mouse.get_position(),mid) / math.pi * 180
    ang = 180 - ang
    # print()
    value = write_read(str(int(ang)))