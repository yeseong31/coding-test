def solution(n):
    dp = [0, 1, 3, 10, 23]
    
    if n <= 4:
        return dp[n]
    
    check = [2, 4, 2]
    tmp = [dp[1] * 2, dp[2] * 2 + dp[1] * 2, dp[3] * 2 + dp[2] * 2 + dp[1] * 4]
    
    for i in range(5, 8):
        dp.append(check[i - 5] + dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5 + tmp[i - 5])
    
    for i in range(8, n + 1):
        result = check[(i + 1) % 3] + dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5 + tmp[(i + 1) % 3]
        k = dp[i - 4] * 2 + dp[i - 5] * 2 + dp[i - 6] * 4
        result += k
        tmp[(i + 1) % 3] += k
        dp.append(result % 1000000007)

    return dp[n]