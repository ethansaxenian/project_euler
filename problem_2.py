from utils import fib


def problem2():
    sum = 0
    i = 0
    while True:
        f = fib(i)
        if f > 4000000:
            break
        elif f % 2 == 0:
            sum += f
        i += 1
    print(sum)
