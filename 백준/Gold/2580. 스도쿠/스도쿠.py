import sys
input = sys.stdin.readline


def check_row(x, k):
    for y in range(9):
        if board[x][y] == k:
            return False
    return True


def check_col(y, k):
    for x in range(9):
        if board[x][y] == k:
            return False
    return True


def check_square(x, y, k):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if board[i][j] == k:
                return False
    return True


def dfs(i):
    if i == len(blank):
        for b in board:
            print(*b)
        exit()
    for n in range(1, 10):
        x, y = blank[i]
        if check_row(x, n) and check_col(y, n) and check_square(x // 3 * 3, y // 3 * 3, n):
            board[x][y] = n
            dfs(i + 1)
            board[x][y] = 0


board = [list(map(int, input().rstrip().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
dfs(0)
