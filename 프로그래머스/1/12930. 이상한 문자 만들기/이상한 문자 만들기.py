def solution(s):
    answer = ''
    idx = 0
    
    for c in s:
        if c == ' ':
            answer += c
            idx = 0
        else:
            answer += c.upper() if idx % 2 == 0 else c.lower()
            idx += 1
    
    return answer
