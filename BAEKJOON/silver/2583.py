# 영역 구하기
import sys
sys.setrecursionlimit(10 ** 4)


def dfs(x, y):
    global count
    if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 0:
        return
    count += 1
    board[x][y] = 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)


m, n, k = map(int, input().split())
board = [[0] * (n + 1) for _ in range(m + 1)]

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    board[x1][y1] += 1
    board[x1][y2] -= 1
    board[x2][y1] -= 1
    board[x2][y2] += 1

for j in range(n + 1):
    for i in range(1, m + 1):
        board[i][j] += board[i - 1][j]

for i in range(m + 1):
    for j in range(1, n + 1):
        board[i][j] += board[i][j - 1]

count = 0
answer = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            count = 0
            dfs(i, j)
            answer.append(count)

print(len(answer))
print(*sorted(answer))
