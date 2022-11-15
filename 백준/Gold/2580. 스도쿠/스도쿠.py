import sys
input = sys.stdin.readline


def solution():
    def dfs(k):
        if k == len(blanks):
            return True
        x, y = blanks[k]
        z = (x // 3 * 3) + y // 3
        for n in range(1, 10):
            if row[x][n] or col[n][y] or block[z][n]:
                continue
            row[x][n] = col[n][y] = block[z][n] = True
            board[x][y] = n
            if dfs(k + 1):
                return True
            row[x][n] = col[n][y] = block[z][n] = False
            board[x][y] = 0
        return False

    board = [list(map(int, input().rstrip().split())) for _ in range(9)]
    blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    row = [[False] * 10 for _ in range(10)]
    col = [[False] * 10 for _ in range(10)]
    block = [[False] * 10 for _ in range(10)]

    for x in range(9):
        for y in range(9):
            z, i = (x // 3 * 3) + y // 3, board[x][y]
            row[x][i] = col[i][y] = block[z][i] = True

    dfs(0)
    for b in board:
        print(*b)


solution()