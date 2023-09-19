from math import ceil


def solution(n, stations, w):
    answer = 0
    area = 2 * w + 1
    
    while n > 0 and stations:
        distance = n - stations[-1] - w
        answer += ceil(distance / area)
        n = stations.pop() - w - 1
        
    answer += ceil(n / area)
    return answer