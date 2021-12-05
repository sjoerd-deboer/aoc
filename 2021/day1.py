def one():
    with open("input-1.txt", "r") as f:
        p = [int(x.strip()) for x in f.readlines()]
        p2 = [(p[y + 1] - p[y]) for y in range(0, len(p) - 1)]
        return sum([x > 0 for x in p2])


def two():
    with open("input-1.txt", "r") as f:
        p = [int(x.strip()) for x in f.readlines()]
        p2 = [(p[y + 2] + p[y + 1] + p[y]) for y in range(0, len(p) - 2)]
        return sum([1 for y in range(1, len(p2)) if (p2[y] > p2[y - 1])])


if __name__ == "__main__":
    print(one())
    print(two())
