from utils import is_palindrome


def problem4():
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i*j) and i*j > max:
                max = i*j
    print(max)
