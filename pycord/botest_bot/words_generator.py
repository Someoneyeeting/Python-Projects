#smoke crack
def Crack(word):
    for i in range(len(word)):
        for j in range(len(word)):
            if i != j:
                if word[i] == word[j]:
                    return False
    return True


def main():
    word = input("Enter a word: ")
    if Crack(word):
        print("The word is a valid word")
    else:
        print("The word is not a valid word")

while True:
    main()