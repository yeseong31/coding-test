def solution(lines):
    def check(start_time):
        end_time = start_time + 1000
        return sum(True for log in logs if log[0] < end_time and log[1] >= start_time)

    answer = 0
    logs = []
    
    for line in lines:
        d, t, s = line.split()
        t = t.split(':')
        s = float(s.replace('s', ''))
        end = (int(t[0]) * 3600 + int(t[1]) * 60 + float(t[2])) * 1000
        start = end - s * 1000 + 1
        logs.append((start, end))

    for target in logs:
        answer = max(answer, check(target[0]), check(target[1]))
    return answer