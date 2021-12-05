input = open("input.txt", "r")


def exercise_one():
    counter = 0
    for line in [x.split() for x in input]:
        count = [int(x) for x in line[0].split("-")]
        password = line[2]
        symbol = password.count(line[1][0])
        correct = symbol in range(count[0], count[1] + 1)
        if correct:
            counter += 1
    return counter


def exercise_two():
    counter = 0
    for line in [x.split() for x in input]:
        indexes = [int(x) for x in line[0].split("-")]
        password = line[2]
        symbol = line[1][0]
        a = password[indexes[0] - 1] == symbol
        b = password[indexes[1] - 1] == symbol
        correct = (a and not b) or (not a and b)
        if correct:
            counter += 1
    return counter


print(exercise_two())
