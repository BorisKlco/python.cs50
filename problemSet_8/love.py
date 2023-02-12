import inflect
import datetime 
from datetime import date

p = inflect.engine()
time = datetime.datetime.now()

def main():
    birth = input('Date:')
    birthY, birthM, birthD = birth.split('-')
    print(birthY, birthM, birthD)
    todayY = time.year
    todayM = time.month
    todayD = time.day

    diff = date(todayY, todayM, todayD) - date(int(birthY), int(birthM), int(todayD))
    print(p.number_to_words(diff.days))



if __name__ == "__main__":
    main()