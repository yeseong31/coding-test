from heapq import heapify, heappop


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = [(v, i) for i, v in enumerate(food_times, 1)]
    heapify(q)
    prev = 0

    while q and (q[0][0] - prev) * len(q) <= k:
        t = heappop(q)[0]
        k -= (t - prev) * (len(q) + 1)
        prev = t
    return sorted(q, key=lambda x: x[1])[k % len(q)][1]
