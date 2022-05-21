# 실전 문제 - 미래 도시(259p)
# 플로이드 워셜

INF = int(1e9)


# 회사 수 n, 경로 수 m
n, m = map(int, input().split())
# 연결된 회사들의 정보
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 경유 노드 x, 목적지 k
x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

print(distance if distance < INF else '-1')

