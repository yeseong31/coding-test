import sys

input = sys.stdin.readline


def dfs(v):
    global cnt
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            cnt += 1
            dfs(i)


# 컴퓨터의 수
n = int(input())
# 간선의 수
m = int(input())
# 그래프
graph = [[] * n for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 기록
visited = set()
cnt = 0

# DFS
dfs(1)
print(cnt)
