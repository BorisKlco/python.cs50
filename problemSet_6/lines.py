import sys

def pythonFile():
    if len(sys.argv) == 1:
        return f'not arg'
    elif len(sys.argv) > 2:
        return f'too many arg'
    else:
        try:
            counter = 0
            with open(sys.argv[1]) as file:
                lines = file.readlines()
                for line in lines:
                    if not line.startswith("#"):
                        if not line.startswith("\n"):
                            counter += 1
                return counter
        except:
            return f"no such file"

print(pythonFile())
