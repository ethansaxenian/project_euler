# PROBLEM 36
from utils import is_palindrome


def problem36():
    palindrome_sum = 0

    for i in range(1000000):
        if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
            palindrome_sum += i

    print(palindrome_sum)
