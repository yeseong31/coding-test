import collections
import sys

input = sys.stdin.readline


def bfs(x):
    q = collections.deque()
    q.append(x)
    visited[x] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
