from ppadb.client import Client as AdbClient
import time
import keyboard

client = AdbClient(host="127.0.0.1", port=5037)
potato = client.device("192.168.100.4:3333")
me = client.device("192.168.100.2:5555")

press = False
pressed = False
while True:
    if(press):
        me.shell("input tap 500 500")

    if(not pressed and keyboard.is_pressed("q")):
        press = not press
        print(press)

    pressed = keyboard.is_pressed("q")
