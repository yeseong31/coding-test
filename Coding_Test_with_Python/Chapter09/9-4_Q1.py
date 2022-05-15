# 실전 문제 - 미래 도시(259p)

import heapq
import sys

# 회사의 개수, 경로의 개수
n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))     # 양방향

# 최종 목적지, 경유 위치
x, k = map(int, input().split())

# 최단 거리 테이블
distance = [INF] * (n + 1)


# 목표: 1 -> K, K -> X의 최단 경로를 구하고, 합한 결과 출력
def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = True
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]


n1 = dijkstra(1, k)
n2 = dijkstra(k, x)
if n1 != INF and n2 != INF:
    print(n1 + n2)
else:
    print(-1)
