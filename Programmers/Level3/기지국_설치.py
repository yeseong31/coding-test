def solution(n, stations, w):
    answer = 0
    t = len(stations) - 1
    area = 2 * w + 1

    while t >= 0 and n > 0:
        target = stations[t]
        if n >= target:
            div, mod = divmod(n - target - w, area)
            answer += div
            if mod:
                answer += 1

        n = target - w - 1
        t -= 1

    if n > 0:
        div, mod = divmod(n, area)
        answer += div
        if mod:
            answer += 1
    return answer


n = 16
stations = [9]
w = 2
print(solution(n, stations, w))


# 효율성 테스트 실패 코드
# def solution(n, stations, w):
#     def check(start, end, station):
#         if start > end:
#             return
#         if not station:
#             return start, end
#         target = station.pop()
#         s, e = target - w, target + w
#         if e < start or end < s:
#             return
#         if s < start:
#             s = start
#         if e > end:
#             e = end
#         remain_area.append(check(start, s - 1, station))
#         remain_area.append(check(e + 1, end, station))
#
#     answer = 0
#     remain_area = []
#     check(1, n, stations)
#
#     for area in remain_area:
#         if area is None:
#             continue
#         answer += math.ceil((area[1] - area[0] + 1) / (2 * w + 1))
#     return answer
