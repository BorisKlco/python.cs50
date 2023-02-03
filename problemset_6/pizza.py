import sys
from tabulate import tabulate
import csv

def pythonFile():
    if len(sys.argv) == 1:
        return f'not arg'
    elif len(sys.argv) > 2:
        return f'too many arg'
    else:
        try:
            if sys.argv[1].endswith(".csv"):
                return pizza(sys.argv[1])
            elif sys.argv[1].endswith(".txt"):
                return f'Not a CSV file'
            else:
                return pizza(f"{sys.argv[1]}.csv")
        except:
            return f'Not a CSV file'

def pizza(file):
    try:
        with open(file) as csvFile:
            reader = csv.DictReader(csvFile)
            grid = []
            for row in reader:
                grid.append( row )
            return tabulate(grid, headers="keys", tablefmt="grid")
    except:
        return f'File does not exist'

print(pythonFile())