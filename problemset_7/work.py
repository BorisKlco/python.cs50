def work():
    return time(input("Time: "))


def time(input):
    h1, h2 = input.split(" to ")
    m1 = h1.split(":")
    m2 = h2.split(":")
    print(m1[0].replace(" AM", ""))
    print(m1[1].replace(" AM", ""))


work()
