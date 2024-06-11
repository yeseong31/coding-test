from math import gcd


def solution(arr):
    answer = arr[0]
    for n in range(1, len(arr)):
        answer *= arr[n] // gcd(answer, arr[n])
    return answer
