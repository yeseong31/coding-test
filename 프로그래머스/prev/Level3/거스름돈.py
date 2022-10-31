def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1

    for m in money:
        for p in range(m, n + 1):
            dp[p] += dp[p - m]

    return dp[n]
