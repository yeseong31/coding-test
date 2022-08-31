# 플로이드(385p)

import sys

input = sys.stdin.readline
flush = sys.stdout.flush

INF = int(1e9)
# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())
# 최단 거리 정보
distance = [[INF] * (n + 1) for _ in range(n + 1)]

# 최단 거리 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < distance[a][b]:
        distance[a][b] = c

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            distance[i][j] = 0

# 거리 계산
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                distance[i][j] = 0
            else:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
