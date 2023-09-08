def solution(dartResult):
    answer = [0]
    
    score = { 'S': '**1', 'D': '**2', 'T': '**3' }
    
    for c in dartResult:
        if c.isdigit():
            answer[-1] = answer[-1] * 10 + int(c)
        elif c in score:
            answer[-1] = eval(f'{answer[-1]}{score[c]}')
            answer.append(0)
        elif c == '*':
            answer[-2] *= 2
            if len(answer) > 2:
                answer[-3] *= 2
        elif c == '#':
            answer[-2] *= -1
            
    return sum(answer)