import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, find):
    q = deque([(start, 0)])
    visited = [False] * (n + 1)
    visited[start] = True
    
    while q:
        v, d = q.popleft()
        
        if v == find:
            return d
        
        for i, l in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append((i, d + l))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))