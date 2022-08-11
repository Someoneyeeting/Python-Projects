import random

def shuffle_text(text):
    shuffled = text.split(" ")
    random.shuffle(shuffled)
    tex = ""
    for i in shuffled:
        tex += i + " "
    return tex

sub_file = open("C:\Program Files (x86)\The Henry Stickmin Collection\ita_english.txt")
sub = sub_file.read()
sub_file.close()
adding = False
split = sub
split = split.split("\n")
for i in split:
    og = i
    i.replace(i[0:i.find("=") + 1] , "")
    i = shuffle_text(i)
    sub.replace(og,i)
    print(og)
    print(i)
    print("\n")



