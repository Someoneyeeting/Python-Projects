def fract(i):
    number = 1
    i = int(i)
    for h in range(i):
        number *= h + 1
    return number
def power(num,pow):
    num = int(num)
    number = int(num)
    pow = int(pow)
    for h in range(pow - 1):
        number *= num
    return number
# while True:
#     num = input("number: ")
#     num = num.split(" ")
#     if(len(num) < 2 or len(num) > 2):
#         print("only 2 numbers")
#         continue
#     print(str(power(num[0],num[1])))

prev = 1
for i in range(30):
    x = 40 + ((i - 1) * -2)
    print(i, x , x - prev)
    prev = x