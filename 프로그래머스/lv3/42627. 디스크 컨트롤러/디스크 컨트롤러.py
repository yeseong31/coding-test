import heapq


def solution(jobs):
    answer = 0
    q = []  # 우선순위 큐
    t = 0  # 소요 시간
    n = len(jobs)  # 작업의 수
    p = -1  # 작업 시작 시간
    success = 0  # 처리한 작업의 수
    
    jobs.reverse()
    
    while success < n:
        # 진입한 작업에 대해 우선순위 큐 구성
        for st, it in jobs:
            if p < st <= t:
                heapq.heappush(q, (it, st))
        if not q:
            t += 1
            continue
        # 우선순위 큐 작업 수행
        it, st = heapq.heappop(q)
        p = t
        t += it
        answer += t - st
        success += 1
    
    return answer // n