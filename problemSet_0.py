import inquirer
import sys
import math

"""
Source: https://cs50.harvard.edu/python/2022/psets/0/

1. Indoor Voice:
    -outputs that same input in lowercase
2. Playback Speed:
    -outputs that same input, replacing each space with ...
3. Making Faces:
    -returns that same input with any :) converted to 🙂, 
    and any :( converted to 🙁
4. Einstein:
    -prompts the user for mass as an integer (in kilograms) 
    and then outputs the equivalent number of Joules as an integer, 
    assume that the user will input an integer
5. Tip Calculator:
    -prompts the user for payed price and calculate 15% tip
"""
try:

    def indoorVoice():
        print("- output will be same as input but in lowercase:")
        userInput = input("\nUser input: ")

        print(f"\nOutput: {userInput.lower()}\n")
        pickProblem()

    def playbackSpeed():
        print("- replacing each space with ... :")
        userInput = input("\nUser input: ")

        userInputReplace = userInput.replace(" ", "...")

        print(f"\nOutput: {userInputReplace}\n")
        pickProblem()

    def makingFaces():
        print("- any :) converted to 🙂, any :( converted to 🙁:")
        userInput = input("\nUser input: ")

        userInputReplaced = userInput.replace(":)", "🙂")
        userInputReplaced = userInputReplaced.replace(":(", "🙁")

        print(f"\nOutput: {userInputReplaced}\n")
        pickProblem()

    def einstein():
        print("- calculator of E=mc2, write mass in kg(m): ")
        userInput = input("\nUser input: ")

        try:
            mass = int(userInput)
            calculation = mass * math.pow(300000000, 2)
            print(f"\nOutput: {int(calculation)}\n")
        except:
            print(f"\nSomething wOoOng?!?1 Try use only whole number.\n")
            pickProblem()

    def tips():
        print("- calculate 15% tip: ")
        userInputPayed = input("\nHow much did you pay? ")
        userInputTip = input("What percentage would you like to tip? ")

        try:
            payed = userInputPayed.replace("$", "")
            tip = userInputTip.replace("%", "")
            calculation = float(payed) * float(tip) / 100
            print(f"\nLeave ${calculation}\n")
        except:
            print(f"\nSomething wOoOng?!?1 Try use only whole number.\n")
            pickProblem()

    def pickProblem():
        problemSet = [
            inquirer.List(
                "problem",
                message="What problem set you wanna run?",
                choices=[
                    "1. Indoor Voice",
                    "2. Playback Speed",
                    "3. Making Faces",
                    "4. Einstein",
                    "5. Tip Calculator",
                    "None, just quit()",
                ],
            ),
        ]

        match inquirer.prompt(problemSet):
            case {"problem": "1. Indoor Voice"}:
                print("Indoor Voice:")
                indoorVoice()
            case {"problem": "2. Playback Speed"}:
                print("Playback Speed:")
                playbackSpeed()
            case {"problem": "3. Making Faces"}:
                print("Making Faces:")
                makingFaces()
            case {"problem": "4. Einstein"}:
                print("Einstein:")
                einstein()
            case {"problem": "5. Tip Calculator"}:
                print("Tip Calculator:")
                tips()
            case {"problem": "None, just quit()"}:
                sys.exit("Bye!")

    pickProblem()

except KeyboardInterrupt:
    sys.exit("\nBye!")
