def one(line1, line2):
    grid = {}
    intersections = []
    num = 1
    for line in (line1, line2):
        start = [0, 0]
        for command in line:
            direction = {"L": [-1, 0], "R": [1, 0], "U": [0, 1], "D": [0, -1]}
            length = int(command[1:])
            step = direction[command[0]]
            for x in range(length):
                start = tuple([sum(p) for p in zip(start, step)])
                if grid.get(start) and grid.get(start) != num:
                    intersections.append(abs(start[0]) + abs(start[1]))
                else:
                    grid[start] = num
        num += 1
    return min(intersections)


def two(line1, line2):
    grid = {}
    intersections = []
    num = 1
    for line in (line1, line2):
        start = [0, 0]
        counter = 1
        for command in line:
            direction = {"L": [-1, 0], "R": [1, 0], "U": [0, 1], "D": [0, -1]}
            length = int(command[1:])
            step = direction[command[0]]
            for x in range(length):
                start = tuple([sum(p) for p in zip(start, step)])
                if grid.get(start) and grid.get(start)[1] != num:
                    intersections.append(grid.get(start)[0] + counter)
                else:
                    grid[start] = [counter, num]
                counter += 1
        num += 1
    return min(intersections)


if __name__ == "__main__":
    with open("input-3.txt", "r") as file:
        f = [y.split(",") for y in [x.strip() for x in file]]
    print(one(f[0], f[1]))
    print(two(f[0], f[1]))
