from utils import amicable


def problem21():
    amicables = []
    for a in range(1,10000):
        for b in range(a, min(10000,2*a)):
            if a != b and amicable(a,b):
                amicables.extend([a,b])
    print(amicables)
    print(sum(amicables))
