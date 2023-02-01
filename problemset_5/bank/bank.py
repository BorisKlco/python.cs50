def main():
    userInput = input("Greeting: ")
    print(helloBank(userInput))

def helloBank(greeting):

    greeting = greeting.strip().lower()

    if greeting.find("hello") == 0:
        return f"$0"
    elif greeting.find("h") == 0:
        return f"$20"
    else:
        return f"$100"
        

if __name__ == "__main__":
    main()