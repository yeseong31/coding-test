def solution(arr):
    INF = int(1e9)
    n = len(arr) // 2 + 1

    min_dp = [[INF] * n for _ in range(n)]
    max_dp = [[-INF] * n for _ in range(n)]
    
    for x in range(n):
        max_dp[x][x] = int(arr[x * 2])
        min_dp[x][x] = int(arr[x * 2])
    
    for step in range(1, n):
        for i in range(n - step):
            j = i + step
            
            for k in range(i, j):
                if arr[k * 2 + 1] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])
                
    
    return max_dp[0][n - 1]
