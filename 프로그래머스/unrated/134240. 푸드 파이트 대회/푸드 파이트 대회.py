import math


def solution(food):
    answer = ''
    
    check = -1
    for i, v in enumerate(food):
        if v == 1 and check == -1:
            check = i
            continue
        answer += str(i) * math.floor(v / 2)
    
    if check > -1:
        answer += str(check) + answer[::-1]
    else:
        answer += answer[::-1]    
    return answer