# 특정한 최단 경로
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance = [INF] * (n + 1)
    distance[s] = 0

    while q:
        dist, v = heapq.heappop(q)
        for i in graph[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

_start = dijkstra(1)
_v1 = dijkstra(v1)
_v2 = dijkstra(v2)

answer = min(_start[v1] + _v1[v2] + _v2[n], _start[v2] + _v2[v1] + _v1[n])
if answer >= INF:
    print(-1)
else:
    print(answer)
