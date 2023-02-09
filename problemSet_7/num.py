def main():
    return validate(input("IP: ").strip())


def validate(ip):
    try:
        one, two, three, four = ip.split(".")
        valid = range(0, 256)
        if (
            int(one) in valid
            and int(two) in valid
            and int(three) in valid
            and int(four) in valid
        ):
            return f"Valid"
        else:
            return f"Invalid"
    except:
        return f"Invalid"


if __name__ == "__main__":
    print(main())
