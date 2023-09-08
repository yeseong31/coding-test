def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    checked = [[0] * (m + 1) for _ in range(n + 1)]
    
    for _type, *points, degree in skill:
        degree *= -1 if _type == 1 else 1
        x1, y1, x2, y2 = points
        checked[x1][y1] += degree
        checked[x2 + 1][y2 + 1] += degree
        checked[x2 + 1][y1] -= degree
        checked[x1][y2 + 1] -= degree
    
    for i in range(1, n + 1):
        for j in range(m):
            checked[i][j] += checked[i - 1][j]
    
    for i in range(n):
        for j in range(1, m + 1):
            checked[i][j] += checked[i][j - 1]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] + checked[i][j] > 0:
                answer += 1
    
    return answer