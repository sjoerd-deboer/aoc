with open("input-9.txt", "r") as f:
    p = [x.strip() for x in f.readlines()]
    low_points = []


def one():
    risk_levels = 0
    for x in range(len(p)):
        for y in range(len(p[x])):
            adjacent = [[a, b] for a, b in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]] if
                        (0 <= a < len(p) and 0 <= b < len(p[x]))]
            is_low = all([int(p[x][y]) < int(p[x1][y1]) for x1, y1 in adjacent])
            if is_low:
                low_points.append((x, y))
                risk_levels += int(p[x][y]) + 1
    return risk_levels


in_a_pool = set()


def two():
    result = sorted([rec(point, len(in_a_pool)) for point in low_points])[-3:]
    return result[0] * result[1] * result[2]


def rec(point, counter=0):
    x, y = point
    adjacent = [[a, b] for a, b in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]] if
                (0 <= a < len(p) and 0 <= b < len(p[x]) and int(p[a][b]) != 9 and int(p[a][b]) > int(p[x][y]) and not (
                                                                                                                          a,
                                                                                                                          b) in in_a_pool)]
    in_a_pool.add((x, y))
    if all(p[a][b] == 9 or p[a][b] in in_a_pool for a, b in adjacent):
        return len(in_a_pool) - counter
    return max([rec(z, counter) for z in adjacent])


if __name__ == "__main__":
    print(one())
    print(two())
