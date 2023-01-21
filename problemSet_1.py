import inquirer
import sys

"""
Source: https://cs50.harvard.edu/python/2022/psets/1/
1. Deep Thought
    implement a program that prompts the user for the answer to the Great Question of Life, 
    the Universe and Everything, outputting Yes if the user inputs 42
    or (case-insensitively) forty-two or forty two. Otherwise output No.
2. Home Federal Savings Bank
    implement a program that prompts the user for a greeting.
    If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), 
    output $20. Otherwise, output $100. Ignore any leading whitespace in the users greeting, 
    and treat the users greeting case-insensitively.
3. File Extensions
    implement a program that prompts the user for the name of a file and then outputs
    that files media type if the files name ends, case-insensitively
4. Math Interpreter
    implement a program that prompts the user for an arithmetic expression and then calculates 
    and outputs the result as a floating-point value formatted to one decimal place.
5. Meal Time
    implement a program that prompts the user for a time and outputs whether its breakfast time, 
    lunch time, or dinner time. If its not time for a meal, dont output anything at all. 

"""

try:
    # 1. Deep Thought
    def deepThought():
        userInput = input(
            "\nWhat is  Great Question of Life, the Universe and Everything? \nUser input: "
        )

        if userInput == "42" or userInput == "forty-two" or userInput == "forty two":
            print("\nYes!\n")
            pickProblem()
        else:
            print("\nno")
            deepThought()

    # 2. Home Federal Savings Bank
    def helloBank():
        userInput = input("\nGreeting: ")

        userInput = userInput.strip().lower()

        if userInput.find("hello") == 0:
            print("\n$0")
            helloBank()
        elif userInput.find("h") == 0:
            print("\n$20")
            helloBank()
        else:
            print("\n$100\n")
            pickProblem()

    # 3. File Extensions
    def files():
        userInput = input("\nName of file and extension: ")

        userInput = userInput.strip().lower()

        if userInput.endswith(".gif"):
            print("\nimage/gif\n")
            pickProblem()
        elif userInput.endswith(".jpg") or userInput.endswith(".jpeg"):
            print("\nimage/jpeg\n")
            pickProblem()
        elif userInput.endswith(".png"):
            print("\nimage/png\n")
            pickProblem()
        elif userInput.endswith(".pdf"):
            print("\napplication/pdf\n")
            pickProblem()
        else:
            print("\napplication/octet-stream")
            files()

    # 4. Math Interpreter
    def math():
        userInput = input("\nExpression: ")
        userInput = userInput.strip().lower().split()

        try:

            x = float(userInput[0])
            y = userInput[1]
            z = float(userInput[2])

            if y == "+":
                print("\n", x + z, "\n")
                pickProblem()
            elif y == "-":
                print("\n", x - z, "\n")
                pickProblem()
            elif y == "*":
                print("\n", x * z, "\n")
                pickProblem()
            elif y == "/":
                print("\n", x / z, "\n")
                pickProblem()
            else:
                print("\nTry again! +,-,*,/\n")
                math()
        except:
            print("\nSomething wrong!")
            math()

    # 5. Meal Time
    def time():
        userInput = input("\nWhat time is it? ")
        userInput = userInput.split(":")

        try:

            timeH = int(userInput[0])
            timeMin = int(userInput[1])

            if timeH == 7 and timeMin <= 60 or timeH == 8 and timeMin == 0:
                print("\nbreakfast time\n")
                time()

            elif timeH == 12 and timeMin <= 60 or timeH == 13 and timeMin == 0:
                print("\lunch time\n")
                time()

            elif timeH == 18 and timeMin <= 60 or timeH == 19 and timeMin == 0:
                print("\ndinner time\n")
                time()

            else:
                print()
                pickProblem()

        except:
            print("\nSomething wrong!")
            time()

    # problemSet_1.py
    def pickProblem():
        problemSet = [
            inquirer.List(
                "problem",
                message="What problem set you wanna run?",
                choices=[
                    "1. Deep Thought",
                    "2. Home Federal Savings Bank",
                    "3. File Extensions",
                    "4. Math Interpreter",
                    "5. Meal Time",
                    "None, just quit()",
                ],
            ),
        ]

        match inquirer.prompt(problemSet):
            case {"problem": "1. Deep Thought"}:
                print("Deep Thought:")
                deepThought()

            case {"problem": "2. Home Federal Savings Bank"}:
                print("Home Federal Savings Bank:")
                helloBank()

            case {"problem": "3. File Extensions"}:
                print("File Extensions:")
                files()

            case {"problem": "4. Math Interpreter"}:
                print("Math Interpreter:")
                math()

            case {"problem": "5. Meal Time"}:
                print("Meal Time:")
                time()

            case {"problem": "None, just quit()"}:
                sys.exit("Bye!")

    pickProblem()

except KeyboardInterrupt:
    sys.exit("\nBye!")
