import keyboard,random


def key(key):
    print(key)

keys = "qwertyuiopasdfghjklzxcvbnm"
for i in keys:
    rand = keys[random.randrange(len(keys))]
    keys.replace(rand,"")
    keyboard.add_hotkey(i,key,args=[i],supress=True)

while True:
    event = keyboard.read_event()
    if(event.event_type != "down"):
        continue
    print(event.name)
