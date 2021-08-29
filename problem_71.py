def problem71():
    rpfs = set()
    for d in range(1, 1000001):
        for n in range(int(d * (3 / 8)), int(d * (3 / 7)) + 1):
            if n / d < 3 / 7:
                rpfs.add(n / d)
    print(sorted(rpfs)[-1])
