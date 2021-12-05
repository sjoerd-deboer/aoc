with open("input-2.txt", "r") as f:
    p = [x.strip().split() for x in f.readlines()]


def one():
    x, depth = (0, 0)
    for command in p:
        if command[0] == "forward":
            x += int(command[1])
        if command[0] == "down":
            depth += int(command[1])
        if command[0] == "up":
            depth -= int(command[1])
    return x * depth


def two():
    x, depth, aim = (0, 0, 0)
    for command in p:
        if command[0] == "forward":
            x += int(command[1])
            depth += aim * int(command[1])
        if command[0] == "down":
            aim += int(command[1])
        if command[0] == "up":
            aim -= int(command[1])
    return x * depth


if __name__ == "__main__":
    print(one())
    print(two())
