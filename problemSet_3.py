import inquirer
import sys
import string

"""
Source: https://cs50.harvard.edu/python/2022/psets/3
1. Fuel Gauge
2. Felipes Taqueria
3. Grocery List
4. Outdated
"""

try:

    # 1. Fuel Gauge
    def fuel():
        userInput = input("Fraction: ")
        fraction = userInput.split("/")

        try:
            gauge = int(fraction[0]) / int(fraction[1]) * 100
            if 100 >= gauge > 99:
                print("F")
            elif 0 <= gauge < 1:
                print("E")
            elif gauge == 25 or gauge == 50 or gauge == 75:
                print(f"{int(gauge)}%\n")
            else:
                fuel()
        except:
            pickProblem()

    # 2. Felipes Taqueria
    def felipe():
        menu = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00,
        }
        order = []
        while True:
            try:
                userInput = input("order: ")
                if userInput in menu:
                    order.append(menu[userInput])
            except EOFError:
                print("finish")
                final = 0
                for price in order:
                    final += price
                print(f"Total: ${final}\n")
                break
        pickProblem()

    # 3. Grocery List
    def list():
        list = {}
        while True:
            try:
                userInput = input()
                userInput = userInput.strip().upper()
                if userInput.isalpha():
                    if userInput not in list:
                        list[userInput] = 1
                    else:
                        add = list[userInput] + 1
                        list[userInput] = add
            except KeyError:
                print("\n")
                return pickProblem()
            except EOFError:
                print("\n")
                for item in list:
                    print(list[item], item)
                print("\n")
                return pickProblem()

    # 4. Outdated
    def outdated():
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        userInput = input("date: ")
        numberDate = userInput.split("/")
        writtenDate = userInput.split(",")
        findingMonth = writtenDate[0].split(" ")
        if (findingMonth[0] in months) and (int(findingMonth[1]) < 32):
            print(
                f"{int(writtenDate[1])}-{int(months.index(findingMonth[0]) + 1):02}-{int(findingMonth[1]):02}"
            )
        elif len(numberDate) == 3 and int(numberDate[1]) < 32:
            print(f"{numberDate[2]}-{int(numberDate[0]):02}-{int(numberDate[1]):02}")
        else:
            print("Out of range\n")
            pickProblem()

    # problemSet_3.py
    def pickProblem():
        problemSet = [
            inquirer.List(
                "problem",
                message="What problem set you wanna run?",
                choices=[
                    "1. Fuel Gauge",
                    "2. Felipes Taqueria",
                    "3. Grocery List",
                    "4. Outdated",
                    "None, just quit()",
                ],
            ),
        ]

        match inquirer.prompt(problemSet):
            case {"problem": "1. Fuel Gauge"}:
                print("Fuel Gauge:")
                fuel()

            case {"problem": "2. Felipes Taqueria"}:
                print("Felipes Taqueria:")
                felipe()

            case {"problem": "3. Grocery List"}:
                print("Grocery List:")
                list()

            case {"problem": "4. Outdated"}:
                print("Outdated:")
                outdated()

            case {"problem": "None, just quit()"}:
                sys.exit("Bye!")

    pickProblem()

except KeyboardInterrupt:
    sys.exit("\nBye!")
