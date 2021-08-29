from utils import is_prime


def quadratic(n, a, b):
    return n ** 2 + a * n + b


def problem27():
    currmax = 0
    coeffs = (0, 0)
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(quadratic(n, a, b)):
                n += 1
            if n > currmax:
                currmax = n
                coeffs = (a, b)
    print(coeffs[0] * coeffs[1])
