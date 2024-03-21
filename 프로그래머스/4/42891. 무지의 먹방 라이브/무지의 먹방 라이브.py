from heapq import heappush, heappop, heapify


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = [(v, i) for i, v in enumerate(food_times, 1)]
    heapify(q)
    
    prev = 0
    
    while q and (q[0][0] - prev) * len(q) <= k:
        target = heappop(q)[0]
        k -= (target - prev) * (len(q) + 1)
        prev = target
    
    return sorted(q, key=lambda x: x[1])[k % len(q)][1]
