import inquirer
import sys
import emoji
from pyfiglet import Figlet
import random

"""
Source: https://cs50.harvard.edu/python/2022/psets/3
1. Emojize
2. Frank,Ian and Glens Letters 
3. Adieu
4. Guessing
5. Professor
6. Bitcoin
"""

try:

    # 1. Emojize
    def emojize():
        userInput = input("emoji text: ")
        print(emoji.emojize(userInput))
        pickProblem()

    # 2. Frank,Ian and Glens Letters
    def frank():
        userInput = input("Input: ")
        figlet = Figlet()
        font = figlet.getFonts()
        if len(sys.argv) < 2:
            randomFont = figlet.setFont(font=font[random.randint(1, 425)])
            print(figlet.renderText(userInput))
        elif sys.argv[1] == "--font" or sys.argv[1] == "-f":
            try:
                figlet.setFont(font=sys.argv[2])
            except:
                randomFont = figlet.setFont(font=font[random.randint(1, 425)])
            print(figlet.renderText(userInput))
        else:
            print("Something WoOoOng?!")

    # 3. Adieu
    def adieu():
        namesList = []

        def insertName(name, names):
            nameList = names
            nameList.append(name)
            return nameList

        while True:
            try:
                userInput = input("\nName: ")
                if userInput != "":
                    insertName(userInput, namesList)
                    print(namesList)
            except EOFError:
                print("\nAdieu, adieu, to", end="")
                for name in namesList[:-2]:
                    print(f" {name},", end="")
                print(f" {namesList[len(namesList) - 2]}", end="")
                if len(namesList) > 1:
                    print(" and", namesList[len(namesList) - 1])
                namesList = []

    # problemSet_4.py
    def pickProblem():
        problemSet = [
            inquirer.List(
                "problem",
                message="What problem set you wanna run?",
                choices=[
                    "1. Emojize",
                    "2. Frank",
                    "3. Adieu",
                    "4. Guessing",
                    "5. Professor",
                    "6. Bitcoin",
                    "None, just quit()",
                ],
            ),
        ]

        match inquirer.prompt(problemSet):
            case {"problem": "1. Emojize"}:
                print("Emojize:")
                emojize()

            case {"problem": "2. Frank"}:
                print("Frank:")
                frank()

            case {"problem": "3. Adieu"}:
                print("Adieu:")
                adieu()

            case {"problem": "4. Guessing"}:
                print("Guessing:")

            case {"problem": "5. Professor"}:
                print("Professor:")

            case {"problem": "6. Bitcoin"}:
                print("Bitcoin:")

            case {"problem": "None, just quit()"}:
                sys.exit("Bye!")

    pickProblem()

except KeyboardInterrupt:
    sys.exit("\nBye!")
