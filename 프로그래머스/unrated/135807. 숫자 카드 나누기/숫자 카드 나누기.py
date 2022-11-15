from math import gcd


def solution(arrayA, arrayB):
    def calcul_gcd(arr):
        result = 0
        for i, x in enumerate(arr):
            if i == 0:
                result = x
                continue
            result = gcd(result, x)
        return result

    def check(arr, target):
        for x in arr:
            if x % target == 0:
                return False
        return True

    answer = []
    a, b = calcul_gcd(arrayA), calcul_gcd(arrayB)

    if check(arrayA, b):
        answer.append(b)
    if check(arrayB, a):
        answer.append(a)

    if len(answer) == 0:
        return 0
    return max(answer)