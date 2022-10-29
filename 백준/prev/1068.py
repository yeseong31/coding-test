# 트리
INF = int(1e9)


def _remove(x):
    graph[x] = INF
    for i in range(n):
        if x == graph[i]:
            _remove(i)


n = int(input())
graph = list(map(int, input().split()))

_remove(int(input()))
answer = 0

for k in range(n):
    if k not in graph and graph[k] != INF:
        answer += 1

print(answer)
