import time

TEST = True
day = 0
file_path = f'data/test{day}.txt' if TEST else f'data/day{day}.txt'

with open(file_path, 'r') as f:
    data = [x.strip() for x in f]
    print(data)


def part_one():
    result = -1
    return result


def part_two():
    result = -1
    return result


if __name__ == '__main__':
    start_time = time.time()
    print(f'The solution for part 1 is: {part_one()} ({time.time() - start_time:.2f}s)')
    start_time = time.time()
    print(f'The solution for part 2 is: {part_two()} ({time.time() - start_time:.2f}s)')
