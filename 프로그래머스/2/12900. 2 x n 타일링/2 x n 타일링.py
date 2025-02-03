def solution(n):
    mod = 1_000_000_007
    dp = list(range(n + 1))

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    
    return dp[n]
