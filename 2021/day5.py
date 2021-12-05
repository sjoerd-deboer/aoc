with open("input-5.txt", "r") as f:
    p = [[[int(z) for z in y.split(",")] for y in x.strip().split(" -> ")] for x in f.readlines()]
    grid = [[0 for y in range(1000)] for x in range(1000)]


def one():
    for line in p:
        line1, line2 = line
        if line1[0] == line2[0] or line1[1] == line2[1]:
            if line2[1] < line1[1] or line2[0] < line1[0]:
                temp = line1
                line1, line2 = line2, temp
            for y in range(line1[0], line2[0] + 1):
                for x in range(line1[1], line2[1] + 1):
                    if grid[x][y] == 0:
                        grid[x][y] = 1
                    else:
                        grid[x][y] += 1
    return sum([len([q for q in x if q > 1]) for x in grid])


def two():
    for line in p:
        line1, line2 = line
        if line1[0] != line2[0] and line1[1] != line2[1]:
            if line2[0] < line1[0]:
                temp = line1
                line1, line2 = line2, temp
            a = 1 if line2[1] > line1[1] else -1
            for y in range(line1[0], line2[0] + 1):
                if grid[line1[1]][y] == 0:
                    grid[line1[1]][y] = 1
                else:
                    grid[line1[1]][y] += 1
                line1[1] += a
    return sum([len([q for q in x if q > 1]) for x in grid])


if __name__ == "__main__":
    print(one())
    print(two())
