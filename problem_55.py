from utils import is_palindrome


def lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True


def problem55():
    print(sum(1 for i in range(10000) if lychrel(i)))
