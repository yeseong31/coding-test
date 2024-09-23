import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, v = heapq.heappop(q)
        if distance[v] < dist:
            continue
        for e, d in graph[v]:
            cost = dist + d
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (cost, e))


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
distance = [INF] * (n + 1)

dijkstra(start)
print(distance[end])