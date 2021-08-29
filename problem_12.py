import sympy


def problem12():
    n = 0
    while True:
        t = (n*(n+1))//2
        if len(sympy.divisors(t)) > 500:
            break
        n += 1
    print(t)
