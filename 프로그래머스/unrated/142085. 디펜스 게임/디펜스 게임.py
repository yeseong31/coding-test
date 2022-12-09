from heapq import heapify, heappush, heappop


def solution(n, k, enemy):
    q = enemy[:k]
    heapify(q)
    for i in range(k, len(enemy)):
        heappush(q, enemy[i])
        n -= heappop(q)
        if n < 0:
            return i
    return len(enemy)