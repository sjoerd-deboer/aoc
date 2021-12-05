with open("input-3.txt", "r") as f:
    p = [x.strip() for x in f.readlines()]


def one():
    tot = [sum([int(x[y]) for x in p]) for y in range(len(p[0]))]
    gamma = "".join(["1" if z > (len(p) // 2) else "0" for z in tot])
    epsilon = "".join(["1" if z == "0" else "0" for z in gamma])
    return int(gamma, 2) * int(epsilon, 2)


def o2():
    z = p.copy()
    for y in range(len(p[0])):
        tot = "1" if sum([int(x[y]) for x in z]) >= len(z) / 2 else "0"
        result = []
        for number in z:
            if len(z) == 1:
                return z[0]
            if number[y] == tot:
                result.append(number)
        z = result.copy()
    return z[0]


def co2():
    z = p.copy()
    for y in range(len(p[0])):
        tot = "0" if sum([int(x[y]) for x in z]) >= len(z) / 2 else "1"
        result = []
        for number in z:
            if len(z) == 1:
                return z[0]
            if number[y] == tot:
                result.append(number)
        z = result.copy()
    return z[0]


def two():
    return int(o2(), 2) * int(co2(), 2)


if __name__ == "__main__":
    print(one())
    print(two())
