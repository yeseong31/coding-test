"""
툭정 거리의 도시 찾기 (339p)

[입력]
4 4 2 1
1 2
1 3
2 3
2 4

[출력]
4
"""


import collections
import sys

input = sys.stdin.readline

# 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발 도시의 번호 x
n, m, k, x = map(int, input().split())
# a번에서 b번으로 이동하는 도로
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단 거리 테이블
distance = [-1] * (n + 1)
# 시작 노드는 거리가 0
distance[x] = 0

# bfs
q = collections.deque([x])
while q:
    node = q.popleft()
    for v in graph[node]:
        # 아직 방문하지 않았다면 최단 거리 갱신
        if distance[v] == -1:
            distance[v] = distance[node] + 1
            q.append(v)

flag = False
for i, d in enumerate(distance):
    if d == k:
        flag = True
        print(i)

if not flag:
    print(-1)
