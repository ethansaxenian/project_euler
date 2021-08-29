def problem29():
    combs = set()
    for a in range(2, 101):
        for b in range(2, 101):
            combs.add(a ** b)
    print(len(combs))
