def one():
    with open("input-2.txt", "r") as file:
        f = [int(z.strip()) for z in [x.split(",") for x in file.readlines()][0]]
        f[1] = 12
        f[2] = 2
        p = 0
        while p < len(f):
            operator = f[p]
            if operator == 99:
                print(f[0])
            elif operator == 1:
                f[f[p + 3]] = f[f[p + 1]] + f[f[p + 2]]
            elif operator == 2:
                f[f[p + 3]] = f[f[p + 1]] * f[f[p + 2]]
            p += 4


with open("input-2.txt", "r") as file:
    inp = [int(z.strip()) for z in [x.split(",") for x in file.readlines()][0]]


def two(parameters: tuple):
    f = inp.copy()
    f[1] = parameters[0]
    f[2] = parameters[1]
    p = 0
    while p < len(f):
        operator = f[p]
        if operator == 99:
            return f[0]
        elif operator == 1:
            f[f[p + 3]] = f[f[p + 1]] + f[f[p + 2]]
        elif operator == 2:
            f[f[p + 3]] = f[f[p + 1]] * f[f[p + 2]]
        p += 4


def _two():
    for x in range(100):
        for y in range(100):
            result = two((x, y))
            if result == 19690720:
                print(100 * x + y)
                return


if __name__ == "__main__":
    one()
    _two()
