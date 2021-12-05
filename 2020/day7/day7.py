with open("input.txt", "r") as input:
    data = [x.strip() for x in input]


# we are looking for the value
def exercise_one(value):
    # create a list of all colors
    all_colors = []
    color_contains = []
    contain_value = []
    # fill all lists
    for x in data:
        y = x.split(" contain ")
        color = y[0].replace(" bags", "")
        if color == value:
            contain_value.append(color)
        else:
            all_colors.append(color)
            z = [" ".join((q.replace(".", "")).split()[1:3]) for q in y[1].split(", ")]
            color_contains.append(z)
    color_contains = dict(zip(all_colors, color_contains))

    # loop through the lists
    change = True
    while change:
        change = False
        for val in contain_value:
            for color in all_colors:
                inside = color_contains[color]
                if val in inside:
                    contain_value.append(color)
                    all_colors.pop(all_colors.index(color))
                    del color_contains[color]
                    change = True
    return len(contain_value) - 1


def exercise_two(color):
    rule = ''
    for line in data:
        if line[:line.index(" bags")] == color:
            rule = line

    print(rule)
    # base case
    if "no" in rule:
        print("no")
        return 1

    rule = rule[rule.index("contain") + 8:].split()

    total = 0
    x = 0
    while x < len(rule):
        count = int(rule[x])
        color = " ".join(rule[x + 1:x + 3])
        # print(rule)
        print(total, color)
        total += count * exercise_two(color)
        x += 4
    return total + 1

    # for y1 in range(0, len(start)):
    #     y = start[y1]
    #     number = int(y.split()[0])
    #     color = " ".join(y.split()[1:])
    #     next = [" ".join([str(int(y[0])*number), y[1], y[2]]) for y in [x.split() for x in color_contains[color]]]
    #     start += next
    #     print("number:", number, "color:", color, "next:", next)
    #     print("start:", start)
    # print("start",start)


print(exercise_one("shiny gold"))
print(exercise_two("shiny gold"))
