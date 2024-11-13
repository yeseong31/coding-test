from math import ceil


def solution(n,a,b):
    cnt = 0
    
    while a != b:
        a, b = ceil(a / 2), ceil(b / 2)
        cnt += 1
    
    return cnt
