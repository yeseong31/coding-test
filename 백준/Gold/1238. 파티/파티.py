import sys
import heapq

input = sys.stdin.readline


def dijkstra(home):
    q = []
    heapq.heappush(q, (0, home))
    distance = [INF] * (n + 1)
    distance[home] = 0

    while q:
        dist, v = heapq.heappop(q)
        for i in graph[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


INF = int(1e9)
n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))


answer = [0] * (n + 1)
for i in range(1, n + 1):
    answer[i] = dijkstra(i)[x]

_x = dijkstra(x)
for j in range(len(_x)):
    answer[j] += _x[j]
    if answer[j] >= INF:
        answer[j] = 0
print(max(answer))