import time
import re
import numpy as np

TEST = False
day = 4
file_path = f'data/test{day}.txt' if TEST else f'data/day{day}.txt'

with open(file_path, 'r') as f:
    data = np.array([list(x.strip()) for x in f])
    data_flipped = np.fliplr(data)


def find_xmas(x): return len(re.findall('(?=(XMAS|SAMX))', "".join(x)))


def part_one():
    result = 0
    for i in range(-(len(data)-1), len(data)):
        result += find_xmas(data.diagonal(i).tolist()) + find_xmas(data_flipped.diagonal(i).tolist())
    for y in range(len(data[0])):
        result += find_xmas(data[y].tolist())
    for x in range(len(data)):
        result += find_xmas([row[x] for row in data])
    return result


def part_two():
    counter = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            cell = data[x][y]
            if cell == 'A':
                if x-1 >= 0 and y-1 >= 0 and x+1 < len(data) and y+1 < len(data[0]):
                    d1 = re.match('MS|SM', str(data[x-1][y-1]) + str(data[x+1][y+1]))
                    d2 = re.match('MS|SM', str(data[x-1][y+1]) + str(data[x+1][y-1]))
                    if d1 and d2:
                        counter += 1
    return counter



if __name__ == '__main__':
    start_time = time.time()
    print(f'The solution for part 1 is: {part_one()} ({time.time() - start_time:.2f}s)')
    start_time = time.time()
    print(f'The solution for part 2 is: {part_two()} ({time.time() - start_time:.2f}s)')
