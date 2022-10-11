# 아기 상어
import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)


def bfs(x, y):
    q = deque([(x, y)])
    dist = [[INF] * n for _ in range(n)]
    dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] == INF and board[nx][ny] <= size:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist


def find_fish(dist):
    x, y, d = 0, 0, INF
    for i in range(n):
        for j in range(n):
            if board[i][j] != -1 and 1 <= board[i][j] < size and dist[i][j] < d:
                x, y, d = i, j, dist[i][j]
    if d == INF:
        return -1
    return x, y, d


n = int(input())
x, y, size = 0, 0, 2

board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            x, y = i, j
            board[i][j] = 0
            break

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
count = 0
answer = 0

while True:
    target = find_fish(bfs(x, y))
    if target == -1:
        break
    x, y, d = target
    answer += d
    board[x][y] = 0
    count += 1
    if size == count:
        count = 0
        size += 1
print(answer)
