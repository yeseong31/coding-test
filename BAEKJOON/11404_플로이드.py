INF = int(1e9)

# 도시의 수
n = int(input())
# 버스의 수
m = int(input())

# 최단 거리 테이블
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            dist[i][j] = 0

# 버스의 정보
for _ in range(m):
    # 시작, 도착, 비용
    a, b, c = map(int, input().split())
    if dist[a][b] > c:
        dist[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
