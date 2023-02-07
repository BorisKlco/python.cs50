import sys


def work():
  return time(input("Time: "))


def time(input):
  try:
    time = []
    h1, h2 = input.split(" to ")
    h1 = h1.replace(" AM", "")
    h2 = h2.replace(" PM", "")

    if ':' in h1:
      h1, m1 = h1.split(":")
      if int(h1) < 12 and int(m1) < 60:
        time.append(f"{h1}:{m1}")
      else:
        sys.exit('bad format AM HM')
    else:
      if int(h1) < 12:
        time.append(f"{h1}:00")
      else:
        sys.exit('bad format AM H')

    if ':' in h2:
      h2, m2 = h2.split(":")
      if int(h2) < 12 and int(m2) < 60:
        time.append(f"{int(h2)+12}:{m2}")
      else:
        sys.exit('bad format PM HM')
    else:
      if int(h2) < 12:
        time.append(f"{int(h2)+12}:00")
      else:
        sys.exit('bad format PM H')

    print(time[0], 'to', time[1])

  except:
    sys.exit('bad format')


work()
