import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(k, v):
    result = 0

    queue = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True

    while queue:
        v = queue.popleft()
        for x, w in graph[v]:
            if w >= k and not visited[x]:
                queue.append(x)
                result += 1
                visited[x] = True

    return result


n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(n - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(m):
    ki, vi = map(int, input().split())
    print(bfs(ki, vi))