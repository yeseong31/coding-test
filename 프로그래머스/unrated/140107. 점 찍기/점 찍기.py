import math


def solution(k, d):
    return sum([1 + math.floor(math.sqrt(d ** 2 - x ** 2)) // k for x in range(0, d + 1, k)])