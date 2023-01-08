# 정점의 수 v, 간선의 수 e
import sys
import collections
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
# 시작 정점 k
k = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    # b(node)까지 c(time)만큼 걸림
    graph[a].append((b, c))

# 소요 시간(time), 정점(node)
q = [(0, k)]
dist = [INF] * (v + 1)
dist[k] = 0

while q:
    time, node = heapq.heappop(q)
    if dist[node] < time:
        continue
    # x(node)까지 y(time)만큼 걸림
    for x, y in graph[node]:
        cost = time + y
        if cost < dist[x]:
            dist[x] = cost
            heapq.heappush(q, (cost, x))

for i in range(1, v + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])