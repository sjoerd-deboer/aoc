with open("input.txt", "r") as input:
    data = [x.strip() for x in input]


def exercise_one(lines):
    result = 0
    for line in lines:
        no_parentheses = remove_parentheses(line, lambda x: calculate(x))
        result += int(calculate(no_parentheses))
    return result


def exercise_two(lines):
    result = 0
    for line in lines:
        no_parentheses = remove_parentheses(line, lambda x: calculate_two(x))
        result += int(calculate(no_parentheses))
    return result


def calculate_two(line):
    x = line.split()
    while "+" in x:
        p = x.index("+")
        x[p - 1] = int(x[p - 1]) + int(x[p + 1])
        del x[p:p + 2]
    while "*" in x:
        p = x.index("*")
        x[p - 1] = int(x[p - 1]) * int(x[p + 1])
        del x[p:p + 2]
    return x[0]


calculate_two("1 + 2 * 3 + 4 * 5 + 6")


def calculate(line):
    x = line.split()
    while len(x) > 1:
        if x[1] == "+":
            x[2] = int(x[0]) + int(x[2])
            del x[0:2]
        else:
            x[2] = int(x[0]) * int(x[2])
            del x[0:2]
    return x[0]


def closing_index(line):
    o, c = 0, 0
    for y in range(0, len(line)):
        x = line[y]
        if x == "(":
            o += 1
        elif x == ")":
            c += 1
            if o == c:
                return y
    return -1


def remove_parentheses(line, calculate):
    if "(" not in line:
        return str(calculate(line))
    closing = closing_index(line)
    p = line[line.index("(") + 1:closing]
    t = line[closing + 1:]
    if line.index("(") == 0:
        if len(t) > 0 and "(" in t:
            return str(calculate(remove_parentheses(p, calculate))) + t[0:3] + str(remove_parentheses(t[3:], calculate))
        else:
            return str(calculate(remove_parentheses(p, calculate))) + t
    else:
        if len(t) > 0 and "(" in t:
            return str(line[0:line.index("(") - 3]) + line[line.index("(") - 3:line.index("(")] + str(
                calculate(remove_parentheses(p, calculate))) + t[0:3] + str(remove_parentheses(t[3:], calculate))
        else:
            return str(line[0:line.index("(") - 3]) + line[line.index("(") - 3:line.index("(")] + str(
                calculate(remove_parentheses(p, calculate))) + t


print(exercise_one(data))
print(exercise_two(data))
