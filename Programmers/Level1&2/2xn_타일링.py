def solution(n):
    # DP 테이블
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 2

    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 1000000007
    return d[n]


print(solution(7))
