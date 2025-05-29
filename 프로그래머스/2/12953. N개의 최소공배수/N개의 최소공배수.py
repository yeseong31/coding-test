from math import gcd


def solution(arr):
    answer = arr[0]
    for n, _ in enumerate(arr):
        answer *= arr[n - 1] // gcd(answer, arr[n - 1])
    return answer
