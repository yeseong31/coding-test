import math


def solution(n, stations, w):
    answer = 0
    area = 2 * w + 1

    while stations and n > 0:
        if stations[-1] - w <= n <= stations[-1] + w:
            n = stations.pop() - w - 1
        if stations:
            answer += math.ceil((n - (stations[-1] + w)) / area)
            n = stations[-1]

    return answer + math.ceil(n / area)