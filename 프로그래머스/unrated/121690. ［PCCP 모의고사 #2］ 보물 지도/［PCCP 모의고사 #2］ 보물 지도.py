from collections import deque


def solution(n, m, hole):
    answer = 0
    
    board = [[0] * (m + 1) for _ in range(n + 1)]
    for x, y in hole:
        board[x][y] = 1
    
    dp = [[[-1, -1] for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1][0] = 0
    
    dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
    outside = lambda x, y: x < 1 or x > n or y < 1 or y > m
    
    q = deque([(1, 1, 0)])
    while q:
        x, y, b = q.popleft()
        for i in range(4):
            for s in range(2):
                if b & s:
                    continue
                nx, ny, nb = x + dx[i] * (s + 1), y + dy[i] * (s + 1), b | s
                if outside(nx, ny) or board[nx][ny] > 0 or dp[nx][ny][nb] != -1:
                    continue
                q.append((nx, ny, nb))
                dp[nx][ny][nb] = dp[x][y][b] + 1
    
    return dp[n][m][0] if dp[n][m][1] == -1 or (dp[n][m][1] > dp[n][m][0] >= 0) else dp[n][m][1]
