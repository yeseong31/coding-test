def solution(s):
    answer = ''
    idx = 0
    for c in s:
        if c == ' ':
            answer += c
            idx = 0
            continue
        if idx % 2 == 0:
            answer += c.upper()
        else:
            answer += c.lower()
        idx += 1
    return answer