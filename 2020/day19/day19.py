with open("test.txt", "r") as input:
    data = [x.strip() for x in input]
    rules = dict([x.split(": ") for x in data[:data.index("")]])
    messages = [x for x in data[data.index("") + 1:]]

counter = 0


def matches_rule(rule, message):
    global counter
    x = rules[rule]
    end_string = '"' in x

    if end_string:
        counter += 1
        print("x", x, "message", message, message[counter - 1] == x[1])
        return message[counter - 1] == x[1]
    print([c for c in x.split()])
    x = x.split()
    if "|" in x:
        return all([matches_rule(y, message) for y in x[:x.index("|")]]) or all(
            [matches_rule(y, message) for y in x[x.index("|") + 1:]])
    else:
        return all([matches_rule(y, message) for y in x])


print(matches_rule('0', "ababbb"))

print(rules)
print(messages)
