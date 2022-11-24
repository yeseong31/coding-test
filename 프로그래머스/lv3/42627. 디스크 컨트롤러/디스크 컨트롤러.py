import heapq


def solution(jobs):
    answer = 0
    q = []
    t = 0
    n = len(jobs)
    p = -1
    success = 0
    
    while success < n:
        for st, it in jobs:
            if p < st <= t:
                heapq.heappush(q, (it, st))
        if not q:
            t += 1
            continue
        it, st = heapq.heappop(q)
        p = t
        t += it
        answer += t - st
        success += 1
    
    return answer // n
