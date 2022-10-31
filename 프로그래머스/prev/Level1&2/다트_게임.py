def solution(dartResult):
    score_area = {
        'S': '**1',
        'D': '**2',
        'T': '**3'
    }

    answer = []
    tmp = ''

    for v in dartResult:
        if v.isdigit():
            tmp += v
        elif v == '*':
            if len(answer) > 1:
                answer[-2] *= 2
            answer[-1] *= 2
        elif v == '#':
            answer[-1] *= -1
        else:
            answer.append(int(eval(tmp + score_area[v])))
            tmp = ''
    return sum(answer)


dartResult = '1S*2T*3S'
print(solution(dartResult))
