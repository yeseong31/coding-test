def solution(rows, columns, queries):
    answer = []
    board = [[columns * i + j + 1 for j in range(columns)] for i in range(rows)]
    
    for query in queries:
        a, b, c, d = (q - 1 for q in query)
        row1, row2 = board[a][b:d], board[c][b + 1:d + 1]
        _min = min(row1 + row2)
        
        for i in range(a, c):
            board[i][b] = board[i + 1][b]
            _min = min(_min, board[i][b])
        for i in range(c, a, -1):
            board[i][d] = board[i - 1][d]
            _min = min(_min, board[i][d])
            
        board[a][b + 1:d + 1], board[c][b:d] = row1, row2
        answer.append(_min)
    
    return answer
