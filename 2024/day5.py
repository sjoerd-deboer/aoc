import time

TEST = False
day = 5
file_path = f'data/test{day}.txt' if TEST else f'data/day{day}.txt'

with open(file_path, 'r') as f:
    data = [x.strip() for x in f]
    rules = [(int(a), int(b)) for a, b in [x.split('|') for x in data[:data.index('')]]]
    updates = [[int(y) for y in x.split(',')] for x in data[data.index('') + 1:]]


class Update(int):

    def __gt__(self, other):
        return (int(other), int(self)) in rules

    def __lt__(self, other):
        return (int(self), int(other)) in rules


def part_one():
    result = 0
    for update in updates:
        if update == sorted([Update(x) for x in update]):
            result += update[int((len(update) - 1) / 2)]
    return result


def part_two():
    result = 0
    for update in updates:
        s = sorted([Update(x) for x in update])
        if update != s:
            result += s[int((len(s) - 1) / 2)]
    return result


if __name__ == '__main__':
    start_time = time.time()
    print(f'The solution for part 1 is: {part_one()} ({time.time() - start_time:.2f}s)')
    start_time = time.time()
    print(f'The solution for part 2 is: {part_two()} ({time.time() - start_time:.2f}s)')
