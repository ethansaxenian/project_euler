from math import sqrt, factorial

import sympy

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def word_value(word):
    return sum(ALPHABET.index(x) for x in word)


def is_prime(n):
    if n < 0:
        return False
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def fib(n):
    return 1 if n in (0, 1) else fib(n - 1) + fib(n - 2)


def is_palindrome(s):
    return str(s) == str(s)[::-1]


def choose(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))


def amicable(a, b):
    if a % b == 0 or b % a == 0:
        return False
    return sum(sympy.divisors(a)[:-1]) == b and sum(sympy.divisors(b)[:-1]) == a
