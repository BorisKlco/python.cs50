import inquirer
import sys
import string

"""
Source: https://cs50.harvard.edu/python/2022/psets/2
1. camelCase
2. Coke Machine
3. Just setting up my twttr
4. Vanity Plates
5. Nutrition Facts
"""

try:

    # 1. camelCase
    def camelCase():
        userInput = input()

        try:
            for char in userInput:
                if char.islower():
                    print(char, end="")
                else:
                    print("_", end="")
                    print(char.lower(), end="")

            print("\n")
            pickProblem()
        except:
            pickProblem()

    # 2. Coke Machine
    def cokeMachine():

        due = 50

        while due > 0:
            print("Amount due:", due)
            userInput = int(input("Insert coins: "))
            due -= userInput
        print("payed")

    # 3. Just setting up my twttr
    def twitter():
        userInput = input("Input: ")
        vowel = ["a", "e", "i", "o", "u"]
        split = []

        print("Output: ", end="")

        for char in userInput:
            split.append(char)

        for letter in split:
            if letter.lower() not in vowel:
                print(letter, end="")

        print("\n")

        pickProblem()

    # 4. Vanity Plates
    def plates():
        userInput = input("Plate: ")

        def zeroCheck(number):
            if "0" in number:
                zero = number.find("0")
                for char in number:
                    if char.isdigit():
                        if zero <= number.index(char):
                            return False
                        return True
            return True

        def middle(mid):
            for number in mid:
                if number.isdigit():
                    lastChar = mid[len(mid) - 1]
                    if lastChar.isdigit():
                        return zeroCheck(mid)
                    else:
                        return False
            else:
                return zeroCheck(mid)

        def is_valid(plate):
            for char in plate:
                if char in string.punctuation:
                    return False
            if plate[0:2].isalpha() and 1 < len(plate) < 7:
                return middle(plate)
            else:
                return False

        if is_valid(userInput):
            print("Valid")
        else:
            print("Invalid")

        print("\n")

        pickProblem()

    # 5. Nutrition Facts
    def nutrition():
        userInput = input("Item: ")
        fruits = [
            {"fruit": "Apple", "cal": "130"},
            {"fruit": "Banana", "cal": "110"},
            {"fruit": "Lemon", "cal": "15"},
            {"fruit": "Peach", "cal": "60"},
            {"fruit": "Strawberries", "cal": "50"},
            {"fruit": "Pineapple", "cal": "50"},
        ]

        for fruit in fruits:
            if fruit["fruit"] == userInput:
                print("Calories:", fruit["cal"])
        print("\n")

        pickProblem()

    # problemSet_2.py
    def pickProblem():
        problemSet = [
            inquirer.List(
                "problem",
                message="What problem set you wanna run?",
                choices=[
                    "1. camelCase",
                    "2. Coke Machine",
                    "3. Just setting up my twttr",
                    "4. Vanity Plates",
                    "5. Nutrition Facts",
                    "None, just quit()",
                ],
            ),
        ]

        match inquirer.prompt(problemSet):
            case {"problem": "1. camelCase"}:
                print("camelCase:")
                camelCase()

            case {"problem": "2. Coke Machine"}:
                print("Coke Machine:")
                cokeMachine()

            case {"problem": "3. Just setting up my twttr"}:
                print("Just setting up my twttr:")
                twitter()

            case {"problem": "4. Vanity Plates"}:
                print("Vanity Plates:")
                plates()

            case {"problem": "5. Nutrition Facts"}:
                print("Nutrition Facts:")
                nutrition()

            case {"problem": "None, just quit()"}:
                sys.exit("Bye!")

    pickProblem()

except KeyboardInterrupt:
    sys.exit("\nBye!")
