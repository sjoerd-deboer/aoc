import time

TEST = False
day = 2
file_path = f'data/test{day}.txt' if TEST else f'data/day{day}.txt'

with open(file_path, 'r') as f:
    data = [[int(z) for z in y] for y in [x.strip().split() for x in f]]
    change = [[y - x for x, y in row] for row in [zip(x[:-1], x[1:]) for x in data]]


def rule1(r): return all(x < 0 for x in r) or all(x > 0 for x in r)


def rule2(r): return min(r) > -4 and max(r) < 4


def part_one():
    return sum([a and b for a, b in zip([rule1(x) for x in change], [rule2(x) for x in change])])


def part_two():
    counter = 0
    for r in data:
        result = []
        for x in range(len(r)):
            sub_row = r[:x] + r[x + 1:]
            c = [y - x for x, y in zip(sub_row[:-1], sub_row[1:])]
            result.append(rule1(c) and rule2(c))
        counter += any(result)
    return counter


if __name__ == '__main__':
    start_time = time.time()
    print(f'The solution for part 1 is: {part_one()} ({time.time() - start_time:.2f}s)')
    start_time = time.time()
    print(f'The solution for part 2 is: {part_two()} ({time.time() - start_time:.2f}s)')
