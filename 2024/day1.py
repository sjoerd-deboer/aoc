import time

TEST = False
day = 1
file_path = f'data/test{day}.txt' if TEST else f'data/day{day}.txt'

with open(file_path, 'r') as f:
    data = [(int(a), int(b)) for a, b in [x.strip().split() for x in f]]
    list1, list2 = zip(*data)

def part_one():
    return sum([abs(a - b) for a, b in zip(sorted(list1), sorted(list2))])

def part_two():
    d = {x: list2.count(x) for x in set(list2)}
    return sum([x * (d.get(x, 0)) for x in list1])

if __name__ == '__main__':
    start_time = time.time()
    print(f'The solution for part 1 is: {part_one()} ({time.time() - start_time:.2f}s)')
    start_time = time.time()
    print(f'The solution for part 2 is: {part_two()} ({time.time() - start_time:.2f}s)')
