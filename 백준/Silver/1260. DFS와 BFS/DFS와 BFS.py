from collections import deque

# 정점의 수 n, 간선의 수 m, 시작 v
n, m, v = map(int, input().split())

# 그래프
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)


def dfs(start, discovered):
    discovered.append(start)
    for i in sorted(graph[start]):
        if i not in discovered:
            dfs(i, discovered)
    return discovered


def bfs(start):
    discovered = [start]
    q = deque([start])
    while q:
        node = q.popleft()
        for i in sorted(graph[node]):
            if i not in discovered:
                q.append(i)
                discovered.append(i)
    return discovered


# DFS와 BFS의 결과 출력
print(*dfs(v, []))
print(*bfs(v))