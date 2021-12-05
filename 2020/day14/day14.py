with open("input.txt") as input:
    data = [x.strip() for x in input]


def exercise_one():
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory = {}
    get_bin = lambda x, n: format(x, 'b').zfill(n)
    apply_mask = lambda x, m: "".join([(b if b != "X" else a) for a, b in zip(x, m)])
    for rule in data:
        if "mask" in rule:
            mask = rule.split(" = ")[1]
        else:
            indx = int(rule[4:rule.index("]")])
            value = int(rule[rule.index("=") + 2:])
            memory[indx] = int(apply_mask(get_bin(value, 36), mask), 2)
    return sum(list(memory.values()))


def exercise_two():
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory = {}
    get_bin = lambda x, n: format(x, 'b').zfill(n)
    apply_mask = lambda x, m: "".join([(b if b != "0" else a) for a, b in zip(x, m)])
    possibilities = lambda i: [int(i, 2)] if "X" not in i else possibilities(i.replace("X", "0", 1)) + possibilities(
        i.replace("X", "1", 1))
    for rule in data:
        if "mask" in rule:
            mask = rule.split(" = ")[1]
        else:
            indx = int(rule[4:rule.index("]")])
            value = int(rule[rule.index("=") + 2:])
            indx2 = apply_mask(get_bin(indx, 36), mask)
            for p in possibilities(indx2):
                memory[p] = value
    return sum(list(memory.values()))


print(exercise_one())
print(exercise_two())
