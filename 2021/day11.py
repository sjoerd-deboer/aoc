with open("input-11.txt", "r") as f:
    p = [[int(y) for y in x.strip()] for x in f.readlines()]


def one():
    flashes = 0
    global p
    for step in range(9999):
        p = [[y + 1 for y in x] for x in p]
        contains_ten = True
        has_popped = set()
        while contains_ten:
            p2 = p.copy()
            contains_ten = False
            for x in range(len(p)):
                for y in range(len(p[x])):
                    if p[x][y] > 9 and (x, y) not in has_popped:
                        if step < 100:
                            flashes += 1
                        has_popped.add((x, y))
                        adjacant = [[a, b] for a, b in
                                    [[x - 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y + 1], [x + 1, y], [x + 1, y - 1],
                                     [x, y - 1], [x - 1, y - 1]] if 0 <= a < len(p) and 0 <= b < len(p[x])]
                        for point in adjacant:
                            p2[point[0]][point[1]] += 1
                            if p2[point[0]][point[1]] == 10:
                                contains_ten = True
            p = p2.copy()
        for x2 in range(len(p)):
            for y2 in range(len(p[x2])):
                if p[x2][y2] > 9:
                    p[x2][y2] = 0
        if not any([any(x) for x in p]):
            return flashes, step


if __name__ == "__main__":
    print(one())
