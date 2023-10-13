import sys

input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(start):
    dist[start] = 0
    
    for x in range(1, n + 1):
        for y in range(m):
            now, _next, cost = edges[y][0], edges[y][1], edges[y][2]
            if dist[now] != INF and dist[_next] > dist[now] + cost:
                dist[_next] = dist[now] + cost
                if x == n:
                    return True
    
    return False


n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

dist = [INF] * (n + 1)
cycle = bellman_ford(1)

if cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        print(dist[i] if dist[i] != INF else -1)
