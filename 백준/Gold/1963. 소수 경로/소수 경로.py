from collections import deque


e = [True] * 10001
for i in range(2, 101):
    if not e[i]:
        continue
    j = i * 2
    while j < 10001:
        e[j] = False
        j += i


def bfs(start, goal):
    q = deque([(start, 0)])
    visited = [False] * 10000
    visited[start] = True
    while q:
        n, cnt = q.popleft()
        if n == goal:
            return cnt
        if n < 1000:
            continue
        for x in [1, 10, 100, 1000]:
            target = n - n % (x * 10) // x * x
            for _ in range(10):
                if not visited[target] and e[target]:
                    visited[target] = True
                    q.append((target, cnt + 1))
                target += x
    return 'Impossible'


for _ in range(int(input())):
    print(bfs(*map(int, input().split())))
