import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def dfs(x, y):
    if visited[x][y]:
        return visited[x][y]

    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] <= board[x][y]:
            continue
        visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)

    return visited[x][y]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
visited = [[0] * n for _ in range(n)]

print(max(dfs(x, y) for x in range(n) for y in range(n) if not visited[x][y]))
