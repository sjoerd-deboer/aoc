with open("input.txt", "r") as input:
    data = [x.replace("\n", " ") for x in input.read().split("\n\n")]


def exercise_one():
    result = []
    for group in data:
        group = group.replace(" ", "")
        uniques = set([x for x in group])
        result.append(len(uniques))
    return sum(result)


def exercise_two():
    result = 0
    for group in data:
        people = group.split()
        uniques = set([x for x in group])
        for question in uniques:
            result += all([(question in x) for x in people])
    return result


print(exercise_one())
print(exercise_two())
