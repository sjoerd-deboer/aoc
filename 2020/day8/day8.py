with open("input.txt", "r") as input:
    data = [x.strip() for x in input]


def exercise_one(input):
    executed = []
    index = 0
    acc = 0
    while index not in executed and index < len(input):
        current = input[index].split()
        operation = current[0]
        argument = current[1]
        executed.append(index)
        index += 1
        if operation == "acc":
            if argument[0] == "+":
                acc += int(argument[1:])
            else:
                acc -= int(argument[1:])
        elif operation == "jmp":
            if argument[0] == "+":
                index += int(argument[1:]) - 1
            else:
                index -= int(argument[1:]) + 1
    return acc, index


def exercise_two():
    one = exercise_one(data)
    executes = (one[1] == len(data))
    index = one[1]
    while not executes or index >= len(data):
        sample = data.copy()
        current = sample[index].split()
        operation = current[0]
        argument = current[1]
        if operation == "nop":
            sample[index] = "jmp " + argument
        elif operation == "jmp":
            sample[index] = "nop " + argument
        index += 1
        one = exercise_one(sample)
        executes = (one[1] == len(data))
    return one[0]


print(exercise_one(data)[0])
print(exercise_two())
