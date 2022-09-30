# 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485
import heapq


def solution(n):
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    check = [[int(1e9)] * n for _ in range(n)]
    q = []

    x = y = 0
    visited[x][y] = True
    check[x][y] = board[x][y]
    heapq.heappush(q, (x, y))

    while q:
        x, y = heapq.heappop(q)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if check[nx][ny] > check[x][y] + board[nx][ny]:
                check[nx][ny] = check[x][y] + board[nx][ny]
                heapq.heappush(q, (nx, ny))

    return check[n - 1][n - 1]


dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f'Problem {cnt}: {solution(n)}')
    cnt += 1
