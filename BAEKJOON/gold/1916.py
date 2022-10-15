# 최소비용 구하기
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


# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 출발점, 도착점
start, end = map(int, input().split())
# 최단 거리 테이블
distance = [INF] * (n + 1)

dijkstra(start)
print(distance[end])
