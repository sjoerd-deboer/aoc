with open("input-12.txt", 'r') as f:
    p = [x.strip() for x in f.readlines()]
    map = {}
    for x in p:
        one, two = x.split("-")
        for a, b in [(one, two), (two, one)]:
            if not map.get(a):
                map[a] = [b]
            else:
                map[a].append(b)


def one(node, visited):
    if node == "end":
        return 1
    if node.islower() and node in visited:
        return 0
    return sum([one(x, visited + node.split()) for x in map[node]])


def two(node, visited, small):
    if node == "end":
        return 1
    if node.islower() and node in visited:
        if not small:
            return sum([two(x, visited + node.split(), True) for x in map[node] if x != "start"])
        else:
            return 0
    return sum([two(x, visited + node.split(), small) for x in map[node] if x != "start"])


if __name__ == "__main__":
    print(one("start", []))
    print(two("start", [], False))
