import heapq


def solution(jobs):
    answer = 0
    # 작업을 담을 우선순위 큐
    q = []
    # 현재 시간
    now = 0
    # 작업 시작 시간
    start = -1
    # 처리한 작업의 양
    cnt = 0

    while cnt < len(jobs):
        # 작업 시간이 짧은 순으로 우선순위 큐 구성
        for st, it in jobs:
            if start < st <= now:
                heapq.heappush(q, (it, st))
        # 작업 시작 시간이 되었다면
        if q:
            it, st = heapq.heappop(q)
            start = now
            now += it
            answer += (now - st)
            cnt += 1
        else:
            now += 1

    return int(answer / len(jobs))


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
