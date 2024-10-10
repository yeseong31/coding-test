import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append((x, y))
    res = [(x, y)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if l <= abs(board[nx][ny] - board[x][y]) <= r:
                visited[nx][ny] = True
                q.append((nx, ny))
                res.append((nx, ny))
    return res


n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            visited[i][j] = True
            area = bfs(i, j)
            if len(area) <= 1:
                continue
            check = True
            target = sum([board[a][b] for a, b in area]) // len(area)
            for a, b in area:
                board[a][b] = target
    if not check:
        break
    answer += 1

print(answer)