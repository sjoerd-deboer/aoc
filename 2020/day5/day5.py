import numpy as np

with open("input.txt", "r") as input:
    data = [x.strip() for x in input]


def binary_search(string, lower_symbol, max):
    min = 0
    for x in string:
        if x == lower_symbol:
            max = (max + min) // 2
        else:
            min = (max + min + 1) // 2
    return min if min == max else -1


def exercise_one():
    result = []
    for line in data:
        row = binary_search(line[0:7], "F", 127)
        col = binary_search(line[7:], "L", 7)
        result.append(row * 8 + col)
    return max(result)


def exercise_two():
    ids = []
    for line in data:
        row = binary_search(line[0:7], "F", 127)
        col = binary_search(line[7:], "L", 7)
        ids.append(row * 8 + col)
    ids.sort()
    difference = [(y - x) for x, y in zip(ids[0:-1], ids[1:])].index(2)
    return ids[difference] + 1


# print(exercise_one())
print(exercise_two())
