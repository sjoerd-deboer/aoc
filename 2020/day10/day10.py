with open("input.txt", "r") as input:
    data = [int(x.strip()) for x in input]
    data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    # data = [1, 3, 6]

print("data", data)


def exercise_one():
    data.sort()
    print(data)
    jolts = [0, 0, 0]
    pointer = 1
    jolts[data[0] - 1] += 1
    while pointer < len(data):
        difference = data[pointer] - data[pointer - 1]
        jolts[difference - 1] += 1
        # print(data[pointer-1], data[pointer], difference)
        pointer += 1
    jolts[2] += 1
    return jolts


def recursion(dictionary, list):
    if len(list) == 0:
        return list[0]

    for x in range(0, len(list)):
        print("2")
        return recursion(dictionary, list[:x] + dictionary[list[x]] + list[x + 1:])


print(recursion({1: [4], 4: [5, 6, 7], 5: [6, 7], 6: [7]}, [1, 4, 5, 6]))


def exercise_two():
    data.append(data[-1] + 3)
    possibilities = {}
    for pointer in range(0, len(data)):
        item = data[pointer]
        possible_next = [x for x in data[pointer + 1:] if (x - data[pointer]) <= 3]
        possibilities[item] = possible_next
    result = [data[0]]


x = exercise_one()
print("x", x)
print(x[0] * x[2])
print(exercise_two())
