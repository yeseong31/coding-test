def solution(n, tops):
    size = n * 3 + 2
    
    dp = [0] * size
    dp[1] = 1
    dp[2] = 2

    for i in range(3, size):
        if i % 3 == 0:
            t = tops[(i // 3) - 1]
            dp[i] = dp[i - 1] + dp[i - 2] if t == 1 else dp[i - 1]
        elif i % 3 == 1:
            t = tops[(i // 3) - 1]
            dp[i] = dp[i - 1] + dp[i - 3] if t == 1 else dp[i - 2] + dp[i - 3]
        else:
            t = tops[((i - 1) // 3) - 1]
            dp[i] = dp[i - 1] + dp[i - 2] if t == 1 else dp[i - 1] + dp[i - 3]
        
        dp[i] %= 10007

    return dp[size - 1]