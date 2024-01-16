def solution(matrix_sizes):
    INF = int(1e9)
    n = len(matrix_sizes)
    
    dp = [[INF] * n for _ in range(n)]
    for x in range(n):
        dp[x][x] = 0
        
    for step in range(1, n):
        for i in range(n):
            j = i + step;
            
            if (n <= j):
                break
                
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][k] + dp[k + 1][j] + (matrix_sizes[i][0] * matrix_sizes[k + 1][0] * matrix_sizes[j][1]))
        
    return dp[0][n - 1]
