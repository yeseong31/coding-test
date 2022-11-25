import sys

from collections import deque

input = sys.stdin.readline


def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or visited[nx][ny] > -1 or board[nx][ny] not in ('.', 'D'):
                continue
            if z == 'S':
                if board[nx][ny] == 'D':
                    return visited[x][y] + 1
                visited[nx][ny] = visited[x][y] + 1
            elif board[nx][ny] == 'D':
                continue
            board[nx][ny] = z
            q.append((nx, ny, z))
            
    return 'KAKTUS'


board = []
r, c = map(int, input().split())

q = deque()
visited = [[-1] * c for _ in range(r)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

for i in range(r):
    row = list(input().strip())
    for j, v in enumerate(row):
        if v == 'S':
            q.append((i, j, v))
            visited[i][j] = 0
            break
    board.append(row)

for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            q.appendleft((i, j, '*'))

print(bfs())