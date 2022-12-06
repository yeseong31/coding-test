from collections import deque


def solution(board):
    n = len(board)
    dist = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]
    q = deque([(0, 0, 0, 0), (0, 0, 3, 0)])
    
    dx = (1, 0, -1, 0)
    dy = (0, -1, 0, 1)
    
    while q:
        x, y, d, c = q.popleft()
        for i in range(4):
            nx, ny, nc = x + dx[i], y + dy[i], c + 100
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
                continue
            if d != i:
                nc += 500
            if dist[nx][ny][i] > nc:
                dist[nx][ny][i] = nc
                q.append((nx, ny, i, nc))

    return min([dist[n - 1][n - 1][i] for i in range(4)])