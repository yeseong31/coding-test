# 무지가 기억한 멜로디, 곡 정보
import math


def solution(m, musicinfos):
    # 제목, 재생된 시간, 시작 시간
    answer = None
    sharp = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for sh in sharp:
        m = m.replace(sh, sharp[sh])

    for info in musicinfos:
        start, end, title, melody = info.split(',')
        # 멜로디 변환
        for sh in sharp:
            melody = melody.replace(sh, sharp[sh])
        # 시간 변환
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        length = end - start
        # 시간 확인 후 melody의 길이 추가
        melody *= math.ceil(length / len(melody))
        # melody 내에 m 문자열이 있는지 확인
        if m not in melody[:length]:
            continue
        # 조건이 일치하면: 재생 시간이 긴 음악, 먼저 입력된 음악 제목 저장
        if answer is None or answer[1] < length or (answer[1] == length and answer[2] > start):
            answer = (title, length, start)
    if answer is None:
        return '(None)'
    return answer[0]


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]
print(solution(m, musicinfos))
