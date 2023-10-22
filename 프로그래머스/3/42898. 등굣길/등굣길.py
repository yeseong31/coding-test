def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    board[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] not in puddles and (i, j) != (0, 0):
                board[i][j] = (board[i - 1][j] + board[i][j - 1]) % 1000000007
    
    return board[-1][-1]