import sys
from collections import deque

input = sys.stdin.readline


def bfs(start: int):
    q = deque([start])
    visited[start] = True
    while q:
        x = q.popleft()
        for p in graph[x]:
            if not visited[p]:
                q.append(p)
                visited[p] = -1 * visited[x]
            if visited[p] == visited[x]:
                return False
    return True


answer = False
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1, n + 1):
        if not visited[i]:
            answer = bfs(i)
            if not answer:
                break
                
    print('YES' if answer else 'NO')