def solution(m, n, puddles):
    # dp 테이블
    d = [[0] * m for _ in range(n)]
    d[0][0] = 1

    # 우물 표시
    for x, y in puddles:
        d[y - 1][x - 1] = -1

    for i in range(n):
        for j in range(m):
            # 웅덩이인 경우
            if d[i][j] == -1:
                d[i][j] = 0
                continue
            # 위가 막혀 있지 않다면
            if i != 0:
                d[i][j] += d[i - 1][j]
            # 왼쪽이 막혀 있지 않다면
            if j != 0:
                d[i][j] += d[i][j - 1]
            d[i][j] %= 1000000007

    return d[n - 1][m - 1]


m, n = 4, 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
