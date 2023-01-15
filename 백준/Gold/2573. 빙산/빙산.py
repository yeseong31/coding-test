import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y, v):
    q = deque([(x, y)])
    next_board = deque()
    v[x][y] = True

    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or v[nx][ny]:
                continue
            if board[nx][ny] != 0:
                v[nx][ny] = True
                q.append((nx, ny))
            else:
                cnt += 1
        if cnt:
            next_board.append((x, y, cnt))
    return next_board


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
answer = 0

while True:
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not visited[i][j]:
                cnt += 1
                melt = bfs(i, j, visited)
                while melt:
                    mx, my, x = melt.popleft()
                    board[mx][my] = max(board[mx][my] - x, 0)
    if cnt == 0:
        answer = 0
        break
    if cnt >= 2:
        break
    answer += 1

print(answer)