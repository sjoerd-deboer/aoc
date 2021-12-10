with open("input-7.txt") as f:
    p = sorted([int(x) for x in f.readline().split(",")])


def one():
    median = p[len(p) // 2]
    return sum([abs(x - median) for x in p])


def two():
    minim, num = float("inf"), -1
    for x in range(min(p), max(p) + 1):
        temp = 0
        for number in p:
            difference = abs(number - x)
            tot = sum([x for x in range(difference + 1)])
            temp += tot
        if temp < minim:
            minim = temp
            num = x
    return minim, num


if __name__ == "__main__":
    print(one())
    print(two())
