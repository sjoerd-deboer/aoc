with open("input-14.txt", "r") as f:
    p = [x.strip() for x in f]
    template, rules = p[:p.index("")][0], p[p.index("") + 1:]
    rules = {a: b for a, b in [x.split(" -> ") for x in rules]}


def one(s):
    global template
    a = {x: template.count(x) for x in rules.keys()}
    d = {}
    for key in rules.keys():
        for char in key:
            if not d.get(char):
                d[char] = template.count(char)
    for step in range(s):
        b = a.copy()
        for q in a.keys():
            if a[q]:
                b[q[0] + rules[q]] += a[q]
                b[rules[q] + q[1]] += a[q]
                d[rules[q]] += a[q]
                b[q] -= a[q]
        a = b.copy()
    return max(d.values()) - min(d.values())


if __name__ == "__main__":
    print(one(10))
    print(one(40))
