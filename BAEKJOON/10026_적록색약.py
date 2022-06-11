import collections


def bfs(x, y, c):
    q = collections.deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if colors[nx][ny] == c:
                visited[nx][ny] = True
                q.append((nx, ny))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input().rstrip())

colors = []
for _ in range(n):
    colors.append(list(input()))

visited = [[False] * n for _ in range(n)]

check = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if colors[i][j] == 'R':
                bfs(i, j, 'R')
            if colors[i][j] == 'G':
                bfs(i, j, 'G')
            if colors[i][j] == 'B':
                bfs(i, j, 'B')
            check += 1

print(check, end=' ')

# 색약일 때
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'

check = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if colors[i][j] == 'R':
                bfs(i, j, 'R')
            if colors[i][j] == 'B':
                bfs(i, j, 'B')
            check += 1

print(check)
