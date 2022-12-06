import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q.append((0, 0))
    visited[0][0] = True
    res = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            # 빈 칸이라면 큐에 삽입
            if board[nx][ny] == 0:
                q.append((nx, ny))
                continue
            # 그렇지 않으면 치즈를 녹임
            board[nx][ny] = 0
            res += 1
    return res


n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

q = deque()
t = 0
prev = []

while True:
    visited = [[False] * m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break
    t += 1
    prev.append(cnt)

print(t)
print(prev[-1])