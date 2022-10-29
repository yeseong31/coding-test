# 트리의 지름
import sys
sys.setrecursionlimit(10 ** 5)


def dfs(node, cost):
    for i in graph[node]:
        v, d = i
        if dist[v] == -1:
            dist[v] = cost + d
            dfs(v, cost + d)


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 1에서부터 가장 먼 길이의 노드 확인
dist = [-1] * (n + 1)
dist[1] = 0
dfs(1, 0)
target = dist.index(max(dist))

# 찾은 노드부터 가장 먼 길이의 노드 확인
dist = [-1] * (n + 1)
dist[target] = 0
dfs(target, 0)
print(max(dist))
