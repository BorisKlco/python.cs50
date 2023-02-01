import inquirer
import sys
import emoji
from pyfiglet import Figlet
import random
import requests

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

    # 4. Guessing Game
    def game():
        gameNumber = random.randint(0, 100)
        while True:
            userInput = input("Guess: ")
            try:
                userNumber = int(userInput)
                if userNumber in range(0, 100):
                    print(gameNumber)
                    if userNumber < gameNumber:
                        print("Too small")
                    elif userNumber > gameNumber:
                        print("Too big")
                    else:
                        print("Right!")
                        return False
                else:
                    print("Guess must be 0-100")
            except:
                print("Guess must be number")

    # 5.Little Proffesor
    def proffesor():
        def getLvl():
            while True:
                try:
                    selectLvl = input("Select Level 1-3: ")
                    if int(selectLvl) in range(1, 4):
                        return selectLvl
                    else:
                        print("Wrong level")
                except:
                    print("Wrong level")

        def generateProblem(level):
            if level == "1":
                return random.randint(0, 9)
            elif level == "2":
                return random.randint(10, 99)
            else:
                return random.randint(100, 999)

        def calculation(a, b):
            hp = 3
            while hp > 0:
                userInput = input(f"{a} + {b} = ")
                if int(userInput) == (a + b):
                    if hp == 3:
                        return 1
                    else:
                        return 0
                else:
                    print("EEE")
                    hp -= 1
            else:
                print(f"{a} + {b} = {a+b}")
                return 0

        level = getLvl()
        score = 0
        round = 0
        while round < 10:
            a = generateProblem(level)
            b = generateProblem(level)
            score = score + calculation(a, b)
            round += 1
        else:
            print(f"Score: {score}")

    # 6. Bitcoin Price Index
    def btc():
        try:
            if sys.argv[1].replace(".", "", 1).isdigit():
                try:
                    req = requests.get(
                        "https://api.coindesk.com/v1/bpi/currentprice.json"
                    )
                    res = req.json()
                    btc = res["bpi"]["USD"]["rate_float"]
                    print(f"${round(float(btc) * float(sys.argv[1]), 2)}")
                except requests.RequestException:
                    print("something")
            else:
                print("not a numb")
        except:
            print("asd")

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
                game()

            case {"problem": "5. Professor"}:
                print("Professor:")
                proffesor()

            case {"problem": "6. Bitcoin"}:
                print("Bitcoin:")
                btc()

            case {"problem": "None, just quit()"}:
                sys.exit("Bye!")

    pickProblem()

except KeyboardInterrupt:
    sys.exit("\nBye!")
