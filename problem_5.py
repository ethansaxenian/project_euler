from math import prod


def divisible(x):
    if x == 0:
        return False
    for i in range(20, 1, -1):
        if x % i != 0:
            return False
    return True


def problem5():
    for i in range(0, prod(range(1, 21)), 20):
        if divisible(i):
            print(i)
            break
