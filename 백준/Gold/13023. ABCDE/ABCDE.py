import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)


def dfs(v, depth):
    global result
    visited[v] = True
    
    if depth == 5:
        result = True
        return
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth + 1)
    
    visited[v] = False


n, m = map(int, input().split())
visited = [False] * n

graph = [[] for _ in range(n)]
result = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in range(n):
    dfs(x, 1)
    if result:
        break

print(1 if result else 0)
