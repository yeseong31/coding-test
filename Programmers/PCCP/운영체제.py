import heapq


def solution(program):
    answer = [0] * 10
    # 우선순위, 호출 시간, 실행 시간
    program.sort(key=lambda x: (x[1], x[0]), reverse=True)
    q = []
    t = 0
    while q or program:
        # 시간이 되었다면 프로세스를 큐에 삽입
        if program and program[-1][1] <= t:
            heapq.heappush(q, (program.pop()))
        # 실행할 프로세스가 없다면 진행하지 않음
        if not q:
            t += 1
            continue
        # 프로세스 실행
        a, b, c = heapq.heappop(q)
        answer[a - 1] += t - b
        # 프로세스 실행 동안 호출된 프로세스 확인
        while program and t <= program[-1][1] <= t + c:
            heapq.heappush(q, (program.pop()))
        t += c

    return [t] + answer

# 코드 개선 이전
# def solution(program):
#     answer = [0] * 10
#     # [(우선순위, 호출 시간, 실행 시간), 인덱스]
#     programs = sorted([(p, i) for i, p in enumerate(program, 1)], key=lambda x: (x[0][1], x[0][0]), reverse=True)
#     q = []
#     t = 0
#     while q or programs:
#         if programs and programs[-1][0][1] <= t:
#             heapq.heappush(q, (programs.pop()))
#         if not q:
#             t += 1
#             continue
#         (priority, call_time, run_time), n = heapq.heappop(q)
#         answer[priority - 1] += t - call_time
#         while programs and t <= programs[-1][0][1] <= t + run_time:
#             heapq.heappush(q, (programs.pop()))
#         t += run_time
#
#     return [t] + answer


# print(solution([[3, 6, 1], [4, 2, 1], [1, 0, 1], [5, 10, 1]]))
print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))
