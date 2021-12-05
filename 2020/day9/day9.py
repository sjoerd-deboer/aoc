import itertools

with open("input.txt", "r") as input:
    data = [int(x.strip()) for x in input]


def exercise_one():
    pointer = 25
    while pointer < len(data):
        current = data[pointer]
        if (pointer - 25) > 0:
            min = pointer - 25
        else:
            min = 0
        range = data[min:pointer]
        combinations = [(x + y) for x, y in list(itertools.combinations(range, 2))]
        if current not in combinations:
            return current
        pointer += 1


def exercise_two():
    value = exercise_one()
    a = 0
    while a < len(data):
        range = [data[a]]
        b = 1
        while sum(range) < value and b < len(data):
            range += [data[a + b]]
            if sum(range) == value:
                return min(range) + max(range)
            b += 1
        a += 1


print(exercise_two())
