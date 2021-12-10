def simulate(d):
    with open("input-6.txt", "r") as f:
        days = [0 for x in range(9)]
        fish = [int(x) for x in f.readline().split(",")]
        for y in fish:
            days[y] += 1
    for day in range(d):
        days.append(days[0])
        del days[0]
        days[6] = days[6] + days[-1]
    return sum(days)


def one():
    return simulate(80)


def two():
    return simulate(256)


if __name__ == "__main__":
    print(one())
    print(two())
