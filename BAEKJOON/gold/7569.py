# 토마토
import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
q = deque()
size = m * n * h

d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
for k in range(h):
    for i in range(n):
        for j in range(m):
            if boxes[k][i][j] == 1:
                q.append((i, j, k, 0))
            elif boxes[k][i][j] == -1:
                size -= 1
answer = -1
while q:
    x, y, z, day = q.popleft()
    size -= 1
    if size == 0:
        answer = day
        break
    for i in range(6):
        nx, ny, nz = x + d[i][0], y + d[i][1], z + d[i][2]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h or boxes[nz][nx][ny] != 0:
            continue
        q.append((nx, ny, nz, day + 1))
        boxes[nz][nx][ny] = 1
print(answer)
