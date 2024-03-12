from math import ceil


def solution(n, stations, w):
    answer = 0
    area = 2 * w + 1
    
    while n > 0 and stations:
        answer += ceil((n - stations[-1] - w) / area)
        n = stations.pop() - w - 1
        
    return answer + ceil(n / area)
