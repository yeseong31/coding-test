# 추석 트래픽
def solution(lines):
    def check(start_time):
        # 임의 시간부터 1초간 처리하는 요청의 최대 개수 확인
        end_time = start_time + 1000

        cnt = 0
        for log in logs:
            # 범위 내에 있는 로그 수 count
            if log[0] < end_time and log[1] >= start_time:
                cnt += 1
        return cnt

    # 초당 최대 처리량
    answer = 0
    # 로그의 '시작시간, 끝시간' 리스트
    logs = []

    for line in lines:
        d, t, s = line.split()
        t = t.split(':')
        s = float(s.replace('s', ''))
        # 밀리초 환산
        end = (int(t[0]) * 3600 + int(t[1]) * 60 + float(t[2])) * 1000
        start = end - s * 1000 + 1
        logs.append((start, end))

    for target in logs:
        answer = max(answer, check(target[0]), check(target[1]))
    return answer


lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines))
