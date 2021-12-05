with open("input.txt", "r") as input:
    grid = [x.strip() for x in input]


def exercise_one(right, left):
    trees = 0
    x, y = 0, 0
    x_max, y_max = len(grid[0]), len(grid)
    while y < y_max:
        if grid[y][x % x_max] == "#":
            trees += 1
        x, y = x + right, y + left
    return trees


def exercise_two(input):
    result = 1
    for x in input:
        result *= exercise_one(x[0], x[1])
    return result


print("1.", exercise_one(3, 1))
print("2.", exercise_two([[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]))
