def solution(n):
    board = [[0] * i for i in range(1, n + 1)]
    dx, dy = (1, 0, -1), (0, 1, -1)
    
    x, y = -1, 0
    step = 1
    for i in range(n):
        for j in range(i, n):
            nx, ny = x + dx[i % 3], y + dy[i % 3]
            board[nx][ny] = step
            x, y, step = nx, ny, step + 1
    
    return [r for row in board for r in row]