from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    pq = []
    time, total_time, idx = 0, 0, 0
    n = len(jobs)
    
    while idx < n or pq:
        while idx < n and jobs[idx][0] <= time:
            req_time, work_time = jobs[idx]
            heappush(pq, (work_time, req_time))
            idx += 1

        if pq:
            work_time, req_time = heappop(pq)
            time += work_time
            total_time += time - req_time
        else:
            time = jobs[idx][0]

    return total_time // n