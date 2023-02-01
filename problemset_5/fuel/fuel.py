def main():
    userInput = input("Fraction: ")
    print(fuel(userInput))

def fuel(input):
    fraction = input.split("/")

    try:
        gauge = int(fraction[0]) / int(fraction[1]) * 100
        if 100 >= gauge > 99:
            return f"F"
        elif 0 <= gauge < 1:
            return f"E"
        elif gauge == 25 or gauge == 50 or gauge == 75:
            return f"{int(gauge)}%"
        else:
            return f"error"
    except:
        return f"error"

if __name__ == "__main__":
    main()