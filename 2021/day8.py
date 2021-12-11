with open("input-8.txt", "r") as f:
    p = [[y.split() for y in x.strip().split(" | ")] for x in f.readlines()]
    solutions = [x[1] for x in p]


def ex_one():
    one, four, seven, eight = (0, 0, 0, 0)
    for solution in solutions:
        for num in solution:
            if len(num) == 2:
                one += 1
            elif len(num) == 4:
                four += 1
            elif len(num) == 3:
                seven += 1
            elif len(num) == 7:
                eight += 1
    return sum([one, four, seven, eight])


def ex_two():
    tot = 0
    for x in p:
        train, result = x
        train = sorted(train, key=len)
        one, four, seven, eight = (train[0], train[2], train[1], train[-1])
        train = train[3:-1]
        nine = [x for x in train if len(set(x).intersection(four)) == 4][0]
        del train[train.index(nine)]
        zero = [x for x in train if (len(set(x).intersection(one)) == 2 and len(set(x).intersection(eight)) == 6)][0]
        del train[train.index(zero)]
        three = [x for x in train if (len(set(x).intersection(one)) == 2 and len(set(x).intersection(eight)) == 5)][0]
        del train[train.index(three)]
        six = [x for x in train if (len(set(x).intersection(one)) == 1 and len(set(x).intersection(eight)) == 6)][0]
        del train[train.index(six)]
        two = [x for x in train if (len(set(x).intersection(nine)) == 4)][0]
        del train[train.index(two)]
        five = train[0]
        train = [set(x) for x in [zero, one, two, three, four, five, six, seven, eight, nine]]
        r = int("".join([str(train.index(set(x))) for x in result]))
        tot += r
    return tot


if __name__ == "__main__":
    print(ex_one())
    print(ex_two())
