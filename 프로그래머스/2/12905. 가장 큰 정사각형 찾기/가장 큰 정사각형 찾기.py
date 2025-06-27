def solution(board):
    answer = 0
    
    row, col = len(board), len(board[0])
    n = max(row, col)
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, len(board) + 1):
        for j in range(1, len(board[0]) + 1):
            if board[i-1][j-1] != 0:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                answer = max(answer, dp[i][j])
    
    return answer ** 2