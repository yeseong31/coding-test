# 실전 문제 - 전보(262p)

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시 수, 통로 수, 메시지 송신 도시
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 최단 거리 테이블
distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

# 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 출력
count = 0
t = 0
for d in distance:
    if d != INF:
        count += 1
        t = max(t, d)

print(count - 1, t)
