letters = [
    "A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","1","2","3","4","5","6","7","8","9","0"
]

password = "mamhoud120051"
cracked = False
len = 1

while not cracked:
    text = ""
    for i in range(len):
        for i in letters:
            text += i
            if text == password:
                cracked = True
                break
            text[-1] = ""
    len += 1
    print(text)
print(len)