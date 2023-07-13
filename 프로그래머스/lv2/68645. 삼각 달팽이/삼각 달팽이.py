def solution(n):
    board = [[0] * i for i in range(1, n + 1)]
    
    x, y, d = -1, 0, 0
    dx, dy = (1, 0, -1), (0, 1, -1)
    cnt = 1
    
    for i in range(n):
        for j in range(i, n):
            d = i % 3
            x, y = x + dx[d], y + dy[d]
            board[x][y] = cnt
            cnt += 1

    return [i for j in board for i in j]