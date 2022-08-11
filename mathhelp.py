from math import *

forces = [(4*sqrt(3),90),(12*sqrt(3),150),(36,300)]
xyforces = [(-8,8*sqrt(3))]

x = 0
y = 0
for i in forces:
    x += i[0] * cos(i[1])
    y += i[0] * sin(i[1])

for i in xyforces:
    x += i[0]
    y += i[1]

force = sqrt((x ** 2) + (y **2))
ang = atan2(x,y)

print(f"x : {x}, y : {y}, force : {force}, ang {ang}")