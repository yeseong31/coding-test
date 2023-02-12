from collections import deque

INF = 100001


def solution(n, k):
    d = [-1] * INF
    d[n] = 0
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            return d[k]
        if 0 < x * 2 < INF and d[x * 2] == -1:
            q.appendleft(x * 2)
            d[x * 2] = d[x]
        if x + 1 < INF and d[x + 1] == -1:
            q.append(x + 1)
            d[x + 1] = d[x] + 1
        if 0 <= x - 1 and d[x - 1] == -1:
            q.append(x - 1)
            d[x - 1] = d[x] + 1


n, k = map(int, input().split())
print(solution(n, k))