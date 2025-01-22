import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
board = [[0] * (n + 1)]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

# 구간 합: 행
for i in range(1, n + 1):
    for j in range(1, n + 1):
        board[i][j] += board[i - 1][j]

# 구간 합: 열
for j in range(1, n + 1):
    for i in range(1, n + 1):
        board[i][j] += board[i][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(board[x2][y2] - board[x2][y1 - 1] - board[x1 - 1][y2] + board[x1 - 1][y1 - 1])