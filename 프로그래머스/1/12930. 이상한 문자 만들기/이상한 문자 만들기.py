def solution(s):
    answer = []
    i = 0
    
    for c in s:
        if c == ' ':
            i = 0
            answer.append(c)
            continue
        
        c = c.upper() if i % 2 == 0 else c.lower()
        answer.append(c)
        i += 1
    
    return ''.join(answer)