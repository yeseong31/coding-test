def solution(n):
    dp = [0, 1, 3, 10, 23]
    
    if n <= 4:
        return dp[n]
    
    check = [2, 4, 2]
    sums = [dp[1] * 2, dp[2] * 2 + dp[1] * 2, dp[3] * 2 + dp[2] * 2 + dp[1] * 4]
    
    for i in range(5, n + 1):
        result = check[(i + 1) % 3] + dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5 + sums[(i + 1) % 3]
        if i >= 8:
            tmp = dp[i - 4] * 2 + dp[i - 5] * 2 + dp[i - 6] * 4
            result += tmp
            sums[(i + 1) % 3] += tmp
        dp.append(result % 1000000007)

    return dp[n]