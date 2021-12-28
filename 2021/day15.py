def print_board(board):
    for row in board:
        print(row)
    print(" ")


with open("test.txt", "r") as f:
    cost = [[int(y) for y in x.strip()] for x in f.readlines()]
    row, col = len(cost), len(cost[0])
    print(row, col)
    # Create the larger board
    cost2 = []
    for x in range(0, 5):
        for row in cost:
            original = [((y + x) % 9) if (y + x) % 9 else 9 for y in row]
            r = []
            for s in range(0, 5):
                for y in original:
                    r.append((y + s) % 9 if (y + s) % 9 else 9)
            cost2.append(r)


def one(cost):
    # print_board(cost)
    row, col = len(cost), len(cost[0])
    tc = [[0 for x in range(col)] for x in range(row)]
    # print_board(tc)
    for i in range(1, row):
        tc[i][0] = tc[i - 1][0] + cost[i][0]
    # print_board(tc)
    for j in range(1, col):
        tc[0][j] = tc[0][j - 1] + cost[0][j]
    # print_board(tc)
    for i in range(1, row):
        for j in range(1, col):
            tc[i][j] = min(tc[i - 1][j], tc[i][j - 1]) + cost[i][j]
    # print_board(tc)
    return tc[row - 1][col - 1]


if __name__ == "__main__":
    # print(one(cost))
    print(one(cost2))
