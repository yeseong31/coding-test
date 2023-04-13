def solution(n):
    dp = [0, 1, 3, 10, 23]
    
    if n <= 4:
        return dp[n]
    
    p = 0
    check = [2, 4, 2]
    sums = [dp[1] * 2, dp[2] * 2 + dp[1] * 2, dp[3] * 2 + dp[2] * 2 + dp[1] * 4]

    for i in range(5, 8):
        dp.append(check[p] + dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5 + sums[p])
        p = (p + 1) % 3

    for i in range(8, n + 1):
        sums[p] += dp[i - 4] * 2 + dp[i - 5] * 2 + dp[i - 6] * 4
        dp.append((check[p] + dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5 + sums[p]) % 1000000007)
        p = (p + 1) % 3

    return dp[n]
