def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    board[0][0] = 1
    
    for x, y in puddles:
        board[y - 1][x - 1] = -1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                board[i][j] = 0
                continue
                
            if i != 0:
                board[i][j] += board[i - 1][j]
            if j != 0:
                board[i][j] += board[i][j - 1]
            
            board[i][j] %= 1_000_000_007
    
    return board[n - 1][m - 1]