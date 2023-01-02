import sys
from collections import deque

INF = int(1e9)
input = sys.stdin.readline


def solution():
    answer = INF
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    n, m = map(int, input().split())
    board = []
    holes = []
    for i in range(n):
        lst = list(map(int, input().strip()))
        for j in range(m):
            if lst[j] == 1:
                holes.append((i, j))
                lst[j] = -1
        board.append(lst)

    visited = [['0'] * m for _ in range(n)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = '1'

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != -1 and visited[nx][ny] != '1':
                board[nx][ny] = dist + 1
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = '1'

    if visited[n - 1][m - 1] == '1':
        answer = min(answer, board[n - 1][m - 1])

    q.append((n - 1, m - 1, 0))
    visited[n - 1][m - 1] = '2'

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == '2':
                continue
            elif board[nx][ny] == -1:
                nnx, nny = nx + dx[i], ny + dy[i]
                if 0 <= nnx < n and 0 <= nny < m and visited[nnx][nny] == '1':
                    answer = min(answer, board[nnx][nny] + dist + 2)
            else:
                board[nx][ny] = dist + 1
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = '2'

    if answer == INF:
        return -1
    return answer + 1


print(solution())
