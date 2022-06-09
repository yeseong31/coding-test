def solution(n):
    if n % 2 == 1:
        return 0

    # DP 테이블
    d = [0] * (n + 1)
    d[2] = 3
    d[4] = 11

    for i in range(6, n + 1, 2):
        # 새로운 결합 형태가 i가 증가함에 따라 2배씩 늘어남
        d[i] = (3 * d[i - 2] + 2 * sum(d[2:i - 2]) + 2) % 1000000007

    return d[n]
