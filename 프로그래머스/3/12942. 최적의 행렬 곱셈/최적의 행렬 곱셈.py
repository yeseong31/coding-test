def solution(matrix_sizes):
    n = len(matrix_sizes)
    INFINITY = 1_000_000_000

    dp = [[INFINITY] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]