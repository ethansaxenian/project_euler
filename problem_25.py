fibs = {0: 0, 1: 1}


def memo_fib(n):
    global fibs
    if n in fibs.keys():
        return fibs[n]
    else:
        return memo_fib(n - 1) + memo_fib(n - 2)


def problem25():
    global fibs
    i = 0
    while True:
        fibs[i] = memo_fib(i)
        if len(str(fibs[i])) == 1000:
            print(i)
            break
        i += 1
