from collections import defaultdict, deque


def solution(board):
    n, m = len(board), len(board[0])
    d = (1, -1)
    visited = [[False] * m for _ in range(n)]
    
    rx = ry = -1
    gx = gy = -1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                continue
            elif board[i][j] == 'G':
                gx, gy = i, j
            elif board[i][j] == 'R':
                rx, ry = i, j
    
    q = deque()
    q.append((rx, ry, 0))
    
    while q:
        x, y, c = q.popleft()
        if x == gx and y == gy:
            return c
        
        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x, y
            
            if i % 2 == 1:
                while 0 <= ny < m and board[nx][ny] != 'D':
                    ny += d[i // 2]
                ny -= d[i // 2]
            else:
                while 0 <= nx < n and board[nx][ny] != 'D':
                    nx += d[i // 2]
                nx -= d[i // 2]
                
            if not visited[nx][ny]:
                q.append((nx, ny, c + 1))
                
    return -1