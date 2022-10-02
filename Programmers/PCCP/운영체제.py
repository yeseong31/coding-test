import heapq


def solution(program):
    answer = [0] * 10
    # [(우선순위, 호출 시간, 실행 시간), 인덱스]
    programs = sorted([(p, i) for i, p in enumerate(program, 1)], key=lambda x: (x[0][1], x[0][0]), reverse=True)
    q = []
    t = 0
    while q or programs:
        # 시간이 되었다면 프로세스를 큐에 삽입
        if programs and programs[-1][0][1] <= t:
            heapq.heappush(q, (programs.pop()))
        # 실행할 프로세스가 없다면 진행하지 않음
        if not q:
            t += 1
            continue
        # 프로세스 실행
        (priority, call_time, run_time), n = heapq.heappop(q)
        answer[priority - 1] += t - call_time
        # 프로세스 실행 동안 호출된 프로세스 확인
        while programs and t <= programs[-1][0][1] <= t + run_time:
            heapq.heappush(q, (programs.pop()))
        t += run_time

    return [t] + answer


# print(solution([[3, 6, 1], [4, 2, 1], [1, 0, 1], [5, 10, 1]]))
print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))
