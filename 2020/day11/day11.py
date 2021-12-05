with open("input.txt") as input:
    data = [list(z) for z in [x.strip() for x in input]]


def isValid(x, y):
    return (y < len(data)) and (x < len(data[0])) and (x >= 0 and y >= 0)


def print_layout(layout):
    for row in layout:
        print("".join(row))


def deep_copy(list):
    result = []
    for a in list:
        row = []
        for b in a:
            row.append(b)
        result.append(row)
    return result


def count_occupied(list):
    return sum([row.count("#") for row in list])


def exercise_one(field):
    new = deep_copy(field)
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            seat = field[y][x]
            adjacent = []
            for x2 in range(-1, 2):
                for y2 in range(-1, 2):
                    if isValid(x + x2, y + y2) and not (x2 == 0 and y2 == 0):
                        adjacent.append(field[y + y2][x + x2])
            if seat == "L" and adjacent.count("#") == 0:
                new[y][x] = "#"
            if seat == "#" and adjacent.count("#") >= 4:
                new[y][x] = "L"
    return new


def exercise_two(field):
    new = deep_copy(field)
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            seat = field[y][x]
            adjacent = []
            if seat != ".":
                for x2 in range(-1, 2):
                    for y2 in range(-1, 2):
                        a, b = x2, y2
                        while True:
                            if not isValid(x + a, y + b) or (a == 0 and b == 0):
                                break
                            if field[y + b][x + a] != ".":
                                adjacent.append(field[y + b][x + a])
                                break
                            a += x2
                            b += y2
            if seat == "L" and adjacent.count("#") == 0:
                new[y][x] = "#"
            if seat == "#" and adjacent.count("#") >= 5:
                new[y][x] = "L"
    return new


result = data
while True:
    changed = exercise_one(result)
    if changed == result:
        break
    result = changed
print("RESULT", count_occupied(result))

result = data
while True:
    changed = exercise_two(result)
    if changed == result:
        break
    result = changed
print("RESULT", count_occupied(result))
