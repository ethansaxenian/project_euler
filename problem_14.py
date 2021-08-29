
lookup = {1: 1}


def collatz(n):
    global lookup
    if n in lookup.keys():
        return lookup[n]
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz(n//2)
    else:
        return 1 + collatz(3*n+1)


def problem14():
    global lookup
    for i in range(1, 1000000):
        lookup[i] = collatz(i)
    print(max(lookup, key=lambda key: lookup[key]))
