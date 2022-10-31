def solution(n):
    v1 = 0
    v2 = 1
    for i in range(3, n + 1):
        v1, v2 = v2, v1 + v2
    return v1 + v2


print(solution(5))
