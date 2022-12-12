def solution(n, money):
    dp = [1] + [0] * n
    for m in money:
        for x in range(m, n + 1):
            dp[x] += dp[x - m]
    return dp[n]