from utils import word_value


def problem22():
    with open("names.txt") as file:
        names = sorted(file.read().replace('"', '').split(','))
    total = 0
    for i in range(len(names)):
        total += word_value(names[i]) * (i + 1)
    print(total)
