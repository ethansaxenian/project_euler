# PROBLEM 35
from utils import is_prime


def rotations(n):
    rotation_list = []
    s = str(n)
    for _ in range(len(s)):
        s = s[1:] + s[0]
        rotation_list.append(s)
    return [int(i) for i in rotation_list]


def problem35():
    primes_found = [2,3,5]

    for i in range(7, 1000000, 2):
        if not any(x in str(i) for x in ["2", "4", "6", "8", "0", "5"]) and i not in primes_found:
            to_check = list(set(rotations(i)))
            if all(is_prime(n) for n in to_check):
                primes_found.extend(to_check)

    print(len(primes_found))
