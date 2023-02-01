import string

def main():
    userInput = input("Plate: ")
    print(plates(userInput))

# 4. Vanity Plates
def plates(input):

    def zeroCheck(number):
        if "0" in number:
            zero = number.find("0")
            for char in number:
                if char.isdigit():
                    if zero <= number.index(char):
                        return False
                    return True
        return True

    def middle(mid):
        for number in mid:
            if number.isdigit():
                lastChar = mid[len(mid) - 1]
                if lastChar.isdigit():
                    return zeroCheck(mid)
                else:
                    return False
        else:
            return zeroCheck(mid)

    def is_valid(plate):
        for char in plate:
            if char in string.punctuation:
                return False
        if plate[0:2].isalpha() and 1 < len(plate) < 7:
            return middle(plate)
        else:
            return False

    if is_valid(input):
        return f"Valid"
    else:
        return f"Invalid"

if __name__ == "__main__":
    main()