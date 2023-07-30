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
        for i in (x - 1, x + 1, x * 2):
            if i < 0 or i > 100000 or d[i] != -1:
                continue
            if i == x * 2:
                d[i] = d[x]
                q.appendleft(i)  # 순간이동이므로 우선 탐색 대상
            else:
                d[i] = d[x] + 1
                q.append(i)


n, k = map(int, input().split())
print(solution(n, k))
