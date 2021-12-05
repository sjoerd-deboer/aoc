def one(i):
    result = []
    for x in range(i[0], i[1]):
        temp = 0
        increasing = True
        for y in str(x):
            if temp > int(y):
                increasing = False
            temp = int(y)
        adjacant = False
        for z in range(0, len(str(x)) - 1):
            if str(x)[z] == str(x)[z + 1]:
                adjacant = True
        if increasing and adjacant:
            result.append(x)
    return len(result)


def two(i):
    result = []
    for x in range(i[0], i[1]):
        temp = 0
        increasing = True
        for y in str(x):
            if temp > int(y):
                increasing = False
            temp = int(y)
        adjacant = False
        for z in range(0, len(str(x)) - 1):
            if str(x)[z] == str(x)[z + 1]:
                if not (z - 1 >= 0 and str(x)[z - 1] == str(x)[z]) and not (
                        z + 2 < len(str(x)) and str(x)[z + 2] == str(x)[z + 1]):
                    adjacant = True
        if increasing and adjacant:
            result.append(x)
    return len(result)


if __name__ == "__main__":
    i = "153517-630395"
    i = [int(x) for x in i.split("-")]
    print(two(i))
