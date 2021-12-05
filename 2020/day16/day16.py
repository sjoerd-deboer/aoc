with open("input.txt", "r") as input:
    data = [x.strip() for x in input if x.strip() != ""]
    rules = [[x.split(": ")[0], x.split(": ")[1].split(" or ")] for x in data[:data.index("your ticket:")]]
    ticket = [int(x) for x in data[data.index("your ticket:") + 1].split(",")]
    nearby = [[int(y) for y in x.split(",")] for x in data[data.index("your ticket:") + 3:]]
    print("rules", rules)
    print("ticket", ticket)
    print("nearby", nearby)


def exercise_one():
    invalid = []
    for ticket in nearby:
        print(is_valid(ticket))
        for field in ticket:
            valid = False
            for rule in rules:
                first = rule[1][0]
                second = rule[1][1]
                temp = field in range(int(first[:first.index("-")]), int(first[first.index("-") + 1:]) + 1) \
                       or field in range(int(second[:second.index("-")]), int(second[second.index("-") + 1:]) + 1)
                if temp:
                    valid = True
            if not valid:
                invalid.append(field)
    return sum(invalid)


def is_valid(ticket):
    for field in ticket:
        valid = False
        for rule in rules:
            first = rule[1][0]
            second = rule[1][1]
            temp = field in range(int(first[:first.index("-")]), int(first[first.index("-") + 1:]) + 1) \
                   or field in range(int(second[:second.index("-")]), int(second[second.index("-") + 1:]) + 1)
            if temp:
                valid = True
        if not valid:
            return False
    return True


def rule_valid(field, rule):
    first = rule[1][0]
    second = rule[1][1]
    return field in range(int(first[:first.index("-")]), int(first[first.index("-") + 1:]) + 1) \
           or field in range(int(second[:second.index("-")]), int(second[second.index("-") + 1:]) + 1)


def exercise_two():
    cols = []
    for x in range(0, len(nearby[0])):
        col = []
        for y in range(0, len(nearby)):
            col.append(nearby[y][x])
        cols.append(col)

    # cols = list(map(list, zip(*nearby)))
    result = {}
    for rule in rules:
        name = rule[0]
        ranges = rule[1]
        print(name, ranges)
        for col in range(0, len(cols)):
            print(cols[col])
            if all([rule_valid(field, rule) for field in cols[col]]):
                result[rule[0]] = result.get(rule[0], []) + [col]

    print(result)
    # solve results
    final = {}
    while len(result) > 0:
        for field in result:
            p = result[field]
            if len(p) == 1:
                final[field] = p[0]
                for f in result:
                    q = result[f]
                    if p[0] in q and len(q) > 1:
                        q.remove(p[0])
                result.pop(field)
                break
        print(final)
    # print(nearby)
    # cols = list(map(list, zip(*nearby)))
    # r = []
    # for col in cols:
    #     p = [int(all([rule_valid(x, rule) for x in col])) for rule in rules]
    #     print("p", p)
    #     r.append(p)
    #     for rule in rules:
    #         result = all([rule_valid(x, rule) for x in col])
    # print(r)
    # import numpy as np
    # arr = np.array(r)
    # print("arr", arr)
    # print("solved", np.linalg.solve(arr, [1]*len(arr)))


# print(exercise_one())
exercise_two()
