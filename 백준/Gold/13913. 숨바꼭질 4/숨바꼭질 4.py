from collections import deque


def solution(n, k):
    if n >= k:
        print(n - k)
        print(*[x for x in range(n, k - 1, -1)])
        return

    inf = max(n, k) + max(n, k) // 2 + 1
    q = deque([n])
    dist, moves = [0] * inf, [0] * inf

    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            prev = x
            answer = []
            for _ in range(dist[x] + 1):
                answer.append(prev)
                prev = moves[prev]
            print(*answer[::-1])
            return
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < inf and not dist[nx]:
                dist[nx] = dist[x] + 1
                moves[nx] = x
                q.append(nx)


n, k = map(int, input().split())
solution(n, k)