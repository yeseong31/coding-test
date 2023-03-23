from heapq import heappush, heappop


def solution(jobs):
    answer = 0
    # 우선순위 큐
    q = []
    # 현재 시간
    t = 0
    # 작업 시작 시간
    s = -1
    # 처리한 프로세스
    p = 0
    
    while p < len(jobs):
        # 요청 시간이 작업 시작 시간과 현재 시간 사이에 있을 때 큐에 삽입
        for st, it in jobs:
            if s < st <= t:
                heappush(q, (it, st))
        # 큐에 프로세스가 있다면
        if q:
            it, st = heappop(q)
            s = t  # 작업 시작 시간 갱신
            t += it  # 현재 시간 갱신
            answer += (t - st)  # 요청~종료 시간 계산
            p += 1
        else:
            t += 1
    
    return answer // len(jobs)