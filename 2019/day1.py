def one():
    with open("input-1.txt", "r") as file:
        file2 = [(int(x.strip()) // 3) - 2 for x in file.readlines() if x != ""]
        print(sum(file2))


def two():
    with open("input-1.txt", "r") as file:
        f = [int(x.strip()) for x in file.readlines()]
        total = 0
        for mod in f:
            mod = (mod // 3) - 2
            while mod > 0:
                total += mod
                mod = (mod // 3) - 2
        print(total)


if __name__ == "__main__":
    one()
    two()
