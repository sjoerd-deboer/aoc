with open("input-13.txt", "r") as f:
    p = [x.strip() for x in f]
    coordinates, instructions = p[:p.index("")], p[p.index("") + 1:]
    coordinates = [[int(y) for y in x.split(",")] for x in coordinates]


def one():
    global coordinates
    for x in [instructions[0]]:
        instruction = x.split()[2]
        axes, position = instruction.split("=")
        result = []
        if axes == "y":
            for point in coordinates:
                if point[1] < int(position) and point not in result:
                    result.append(point)
                else:
                    distance = point[1] - int(position)
                    new_point = [point[0], int(position) - distance]
                    if new_point not in result:
                        result.append(new_point)
        else:
            for point in coordinates:
                if point[0] < int(position):
                    if point not in result:
                        result.append(point)
                else:
                    distance = point[0] - int(position)
                    new_point = [int(position) - distance, point[1]]
                    if new_point not in result:
                        result.append(new_point)
        coordinates = result
    return len(coordinates)


def two():
    global coordinates
    for x in instructions:
        instruction = x.split()[2]
        axes, position = instruction.split("=")
        result = []
        if axes == "y":
            for point in coordinates:
                if point[1] < int(position) and point not in result:
                    result.append(point)
                else:
                    distance = point[1] - int(position)
                    new_point = [point[0], int(position) - distance]
                    if new_point not in result:
                        result.append(new_point)
        else:
            for point in coordinates:
                if point[0] < int(position):
                    if point not in result:
                        result.append(point)
                else:
                    distance = point[0] - int(position)
                    new_point = [int(position) - distance, point[1]]
                    if new_point not in result:
                        result.append(new_point)
        coordinates = result
    return len(coordinates)


if __name__ == "__main__":
    print(two())
    xs = [x[0] for x in coordinates]
    ys = [y[1] for y in coordinates]
    for x in range(min(xs), max(xs)):
        print(["#" if [x, y] in coordinates else "." for y in range(min(ys), max(ys))])
