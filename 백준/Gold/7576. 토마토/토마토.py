import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
q = deque()
size = m * n

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

box = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        if lst[j] == 1:
            q.append((i, j, 0))
        elif lst[j] == -1:
            size -= 1
    box.append(lst)

answer = -1
while q:
    x, y, day = q.popleft()
    size -= 1
    if size == 0:
        answer = day
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or box[nx][ny] != 0:
            continue
        q.append((nx, ny, day + 1))
        box[nx][ny] = 1
print(answer)