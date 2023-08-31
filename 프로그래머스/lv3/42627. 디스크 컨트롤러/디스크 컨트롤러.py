from heapq import heappush, heappop


def solution(jobs):
    answer = 0
    length = len(jobs)
    q = []

    jobs.sort(key=lambda x: -x[0])

    t = 0
    while jobs or q:

        while jobs and jobs[-1][0] <= t:
            target = jobs.pop()
            heappush(q, (target[1], target[0]))

        if q and t >= q[0][1]:
            work_time, start_time = heappop(q)
            end_time = t + work_time
            answer += end_time - start_time
            t = end_time
        else:
            t += 1

    return answer // length
