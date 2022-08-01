from collections import deque

# 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각
# - 같인 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다.
# - 모든 인원은 23:59 전에는 집에 도착해야 함

# 셔틀 운행 횟수, 운행 간격, 셔틀에 탈 수 있는 최대 크루 수, 크루가 대기열에 도착하는 시각


def solution(n, t, m, timetable):
    answer = 0

    q = deque(sorted([int(tt[:2]) * 60 + int(tt[3:]) for tt in timetable]))

    # 9시부터 t분 간격으로 n회 운행
    lst = []
    start = 540
    while n > 0 and q:
        # 현재 시간에 기다리고 있는 인원 최대 m명 추출
        tmp = []
        for i in range(m):
            if not q or q[0] > start:
                break
            tmp.append(q.popleft())
        lst.append((start, tmp))
        start += t
        n -= 1

    last_bus_time, crew = lst[-1]
    if len(crew) < m:
        answer = max(answer, last_bus_time)
    else:
        answer = crew[-1] - 1

    div, mod = divmod(answer, 60)
    div = '0' + str(div) if div < 10 else str(div)
    mod = '0' + str(mod) if mod < 10 else str(mod)
    return f'{div}:{mod}'


n, t, m = 1, 1, 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))

n, t, m = 2, 10, 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))

n, t, m = 2, 1, 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
print(solution(n, t, m, timetable))

n, t, m = 1, 1, 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(solution(n, t, m, timetable))

n, t, m = 1, 1, 1
timetable = ["23:59"]
print(solution(n, t, m, timetable))

n, t, m = 10, 60, 45
timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(solution(n, t, m, timetable))

