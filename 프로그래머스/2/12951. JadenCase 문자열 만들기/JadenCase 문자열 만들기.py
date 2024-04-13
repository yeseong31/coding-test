def solution(s):
    answer = ''
    i = 0
    start = False
    
    while i < len(s):
        c = s[i]
        
        if c == ' ':
            answer += c
            start = False
        elif not start:
            answer += c.upper()
            start = True
        else:
            answer += c.lower()
        i += 1
        
    return answer
