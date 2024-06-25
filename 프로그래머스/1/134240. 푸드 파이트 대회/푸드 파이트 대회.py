import math


def solution(food):
    answer = ''
    
    check = -1
    for i, v in enumerate(food):
        if v == 1 and check == -1:
            check = i
        else:
            answer += str(i) * math.floor(v / 2)
    
    answer += answer[::-1] if check <= -1 else str(check) + answer[::-1]
    return answer