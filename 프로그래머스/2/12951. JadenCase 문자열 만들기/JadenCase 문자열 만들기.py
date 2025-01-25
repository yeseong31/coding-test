def solution(s):
    answer = []
    start = False
    
    for c in s:
        if c == ' ':
            start = False
        elif start:
            c = c.lower()
        else:
            c = c.upper()
            start = True
        
        answer.append(c)
        
    return ''.join(answer)
