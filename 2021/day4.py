class Board:
    grid = []

    def __init__(self, grid):
        self.grid = [[int(y) for y in x.split()] for x in grid]
        self.marked = [[False for i in range(5)] for j in range(5)]

    def checkNumber(self, number):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if self.grid[x][y] == number:
                    self.marked[x][y] = True

    def hasARow(self):
        for row in self.marked:
            if all(row):
                return True
        return False

    def hasAColumn(self):
        for z in range(len(self.marked[0])):
            if all([q[z] for q in self.marked]):
                return True
        return False

    def hasWon(self):
        return self.hasARow() or self.hasAColumn()

    def score(self):
        total = 0
        for x in range(len(self.marked)):
            for y in range(len(self.marked[0])):
                if not self.marked[x][y]:
                    total += self.grid[x][y]
        return total


with open("input-4.txt", "r") as f:
    p = f.readlines()
    numbers = [int(x) for x in p[0].split(",")]
    p = [x.strip() for x in p[2:] if x != "\n"]
    z = [p[x:x + 5] for x in range(0, len(p) - 4, 5)]
    boards = [Board(x) for x in z]


def one():
    for number in numbers:
        for board in boards:
            board.checkNumber(number)
            if board.hasWon():
                return board.score() * number


def two():
    for number in numbers:
        for board in boards:
            board.checkNumber(number)
            if board.hasWon():
                if sum([x.hasWon() for x in boards]) == len(boards):
                    return board.score() * number


if __name__ == "__main__":
    print(one())
    print(two())
