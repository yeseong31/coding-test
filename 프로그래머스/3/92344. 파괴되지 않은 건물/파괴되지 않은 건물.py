def solution(board, skill):
    n, m = len(board), len(board[0])
    checked = [[0] * (m + 1) for _ in range(n + 1)]
    
    for t, *p, d in skill:
        d *= -1 if t == 1 else 1
        x1, y1, x2, y2 = p
        checked[x1][y1] += d
        checked[x2 + 1][y2 + 1] += d
        checked[x2 + 1][y1] -= d
        checked[x1][y2 + 1] -= d
    
    for i in range(1, n + 1):
        for j in range(m):
            checked[i][j] += checked[i - 1][j]
    
    for i in range(n):
        for j in range(1, m + 1):
            checked[i][j] += checked[i][j - 1]
    
    return sum(board[i][j] + checked[i][j] > 0 for i in range(n) for j in range(m))
