import itertools

from utils import is_prime


def problem41():
    primes = []
    for i in range(1, 10):
        digits = list(range(1, i + 1))
        nums = itertools.permutations(digits, len(digits))
        for n in nums:
            num = int(''.join(map(str, n)))
            if is_prime(num):
                primes.append(num)
    print(max(primes))
