def main():
    userInput = input("Input: ")
    print(twttr(userInput))

def twttr(userInput):
    #userInput = input("Input: ")
    vowel = ["a", "e", "i", "o", "u"]
    twt = userInput

    for letter in userInput:
        if letter.lower() in vowel:
            twt = twt.translate({ord(letter): None})
    
    return twt

if __name__ == "__main__":
    main()