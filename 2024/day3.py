import time
import re

TEST = False
day = 3
file_path = f'data/test{day}.txt' if TEST else f'data/day{day}.txt'

with open(file_path, 'r') as f:
    data = "do()"+"".join([x.strip() for x in f])+"don't()"

def part_one():
    return sum([(int(a)*int(b)) for a, b in re.findall('mul\((\d*),(\d*)\)', data)])

def part_two():
    return sum([sum([(int(a) * int(b)) for a, b in re.findall('mul\((\d*),(\d*)\)', block)]) for block in re.findall('do\(\)(.*?)don\'t\(\)', data)])


if __name__ == '__main__':
    start_time = time.time()
    print(f'The solution for part 1 is: {part_one()} ({time.time() - start_time:.2f}s)')
    start_time = time.time()
    print(f'The solution for part 2 is: {part_two()} ({time.time() - start_time:.2f}s)')
