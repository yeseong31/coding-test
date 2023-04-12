def get_seconds(t: str) -> int:
    return int(t[:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:])


def seconds_to_time(s: int) -> str:
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}'


def solution(play_time, adv_time, logs):
    # 동영상 재생시간과 공익광고 재생시간이 같은 경우
    if play_time == adv_time:
        return '00:00:00'
    play_time, adv_time = get_seconds(play_time), get_seconds(adv_time)
    # 누적 합
    views = [0] * (play_time + 1)
    for log in logs:
        start, end = log.split('-')
        views[get_seconds(start)] += 1
        views[get_seconds(end)] -= 1
    for i in range(1, play_time):
        views[i] += views[i - 1]
    for i in range(1, play_time):
        views[i] += views[i - 1]
    # 시청자가 가장 많은 구간 확인
    answer, _max = 0, -1
    for i in range(adv_time - 1, play_time):
        target = views[i] - views[i - adv_time]
        if _max < target:
            _max = target
            answer = i - adv_time + 1
    return seconds_to_time(answer)