import inquirer
import sys
import string

"""
Source: https://cs50.harvard.edu/python/2022/psets/2
1. camelCase
2. Coke Machine
3. Just setting up my twttr
4. Vanity Plates
5. Meal Time
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

    # 3. Vanity Plates
    def plates():
        userInput = input("Plate: ")

        def is_valid(plate):
            for char in plate:
                if char in string.punctuation:
                    return False
            if plate[0:2].isalpha() and 1 < len(plate) < 7:
                """
                if len(plate) == 6:
                    if plate[3:5].isdigit() and plate[6].isalpha():
                        print(plate[2].isdigit())
                        print(plate[3].isdigit())
                        return False
                    else:
                        return True
                if len(plate) < 6:
                    if plate[2].isdigit():
                        print(plate[2].isdigit())
                        return False

                    else:
                        return True
                """
            else:
                return False

        if is_valid(userInput):
            print("Valid")
        else:
            print("Invalid")

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
                    "5. Meal Time",
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

            case {"problem": "5. Meal Time"}:
                print("Meal Time:")

            case {"problem": "None, just quit()"}:
                sys.exit("Bye!")

    pickProblem()

except KeyboardInterrupt:
    sys.exit("\nBye!")
