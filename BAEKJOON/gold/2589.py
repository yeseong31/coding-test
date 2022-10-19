# 보물섬
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input() for _ in range(n)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 'W' or visited[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    return visited[x][y] - 1


answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            if 1 <= i < n - 1 and board[i - 1][j] == board[i + 1][j] == 'L':
                continue
            if 1 <= j < m - 1 and board[i][j - 1] == board[i][j + 1] == 'L':
                continue
            answer = max(answer, bfs(i, j))
print(answer)
