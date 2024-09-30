""" 2178번: 미로 탐색 """

# 두 정수 n, m
import collections

n, m = map(int, input().split())
# n개의 줄에는 m개의 정수
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = collections.deque()
    q.append((x, y))

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                q.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
