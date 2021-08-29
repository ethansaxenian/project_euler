import sympy

from utils import word_value


def problem42():
    triangles = []
    n = sympy.Symbol('n')
    with open("words.txt") as file:
        words = sorted(file.read().replace('"', '').split(','))
    for word in words:
        ans = sympy.solve((1 / 2) * n * (n + 1) - word_value(word), n)
        x = [a for a in ans if a > 0 and float(a).is_integer()]
        if x:
            triangles.append(word)
    print(len(triangles))
