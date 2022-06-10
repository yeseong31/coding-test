import collections


def bfs(start):
    q = collections.deque()
    q.append(start)

    while q:
        v = q.popleft()
        if v == k:
            return d[v]
        for x in [v - 1, v + 1, 2 * v]:
            if x < 0 or x > 100000:
                continue
            if not d[x]:
                d[x] = d[v] + 1
                q.append(x)


# 출발지, 목적지
n, k = map(int, input().split())
# 거리 테이블
d = [0] * 100001

print(bfs(n))
