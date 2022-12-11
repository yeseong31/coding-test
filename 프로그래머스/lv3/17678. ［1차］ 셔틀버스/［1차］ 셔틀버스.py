def solution(n, t, m, timetable):
    answer = []
    crews = [int(x[:2]) * 60 + int(x[3:]) for x in sorted(timetable, reverse=True)]
    
    for depart_time in [9 * 60 + i for i in range(0, n * t, t)]:
        cnt, prev = 0, depart_time
        while crews and crews[-1] <= depart_time and cnt < m:
            prev = crews.pop()
            cnt += 1
        answer.append((depart_time, cnt, prev))
    
    if answer[-1][1] < m:
        target = answer[-1][0]
    else:
        target = answer[-1][2] - 1
    div, mod = map(str, divmod(target, 60))
    return div.zfill(2) + ':' + mod.zfill(2)