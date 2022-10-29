import collections
import sys
input = sys.stdin.readline


def bfs(x):
    q = collections.deque()
    q.append(x)
    visited[x] = x

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = v


n = int(input())

graph = [[0] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
bfs(1)

for v in visited[2:]:
    print(v)
