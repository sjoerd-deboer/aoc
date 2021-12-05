input = open("input.txt", "r")
numbers = sorted([int(x.strip()) for x in input])
for x in numbers:
    for y in numbers:
        for z in numbers:
            if x + y + z == 2020:
                print(x * y * z)
                break
