def problem56():
    max = 0
    for a in range(100):
        for b in range(100):
            dsum = sum(int(i) for i in str(a ** b))
            if dsum > max:
                max = dsum
    print(max)
