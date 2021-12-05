import numpy as np

with open("test.txt", "r") as input:
    data = [[p for p in x.strip()] for x in input]
print("data", data)


def isValid(x, y, z, s):
    return x >= 0 and y >= 0 and z >= 0 and x < s and y < s and z < s


def findNeighbors(x, y, z, s):
    return [q for q in [[x + 1, y, z], [x - 1, y, z], [x, y + 1, z], [x, y - 1, z], [x, y, z + 1], [x, y, z - 1]] if
            isValid(q[0], q[1], q[2], s)]


def checkNeighbors(x, y, z, s, cube):
    n = findNeighbors(x, y, z, s)
    p = [int(cube[p[2]][p[1]][p[0]]) for p in n]
    return sum(p)


def exercise_one():
    # first cycle
    cubeSize = len(data[0])
    cube = np.zeros((cubeSize, cubeSize, cubeSize))
    # z,y,x
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if data[y][x] == "#":
                cube[1][y][x] = 1

    # check neighbouring
    result = cube.copy()
    for z in range(0, cubeSize):
        for y in range(0, cubeSize):
            for x in range(0, cubeSize):
                c = cube[z][y][x]
                active_neighbors = checkNeighbors(x, y, z, cubeSize, cube)
                if c == 1:
                    if active_neighbors < 2 or active_neighbors > 3:
                        # becomes inactive
                        result[z][y][x] = 0
                elif c == 0:
                    if active_neighbors == 3:
                        # becomes active
                        result[z][y][x] = 1

                print((z, y, x), active_neighbors)

    print()
    print(cube)
    print(result)


exercise_one()
