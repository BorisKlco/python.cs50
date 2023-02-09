import validators


def userInput():
    return validate(input("Email: "))


def validate(mail):
    if validators.email(mail):
        return f"Valid"
    else:
        return f"Invalid"


if __name__ == "__main__":
    print(userInput())
