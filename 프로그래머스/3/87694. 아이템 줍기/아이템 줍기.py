from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    
    board = [[-1] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]
    
    for r in rectangle:
        lx, ly, rx, ry = map(lambda x: x * 2, r)
        
        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                if lx < x < rx and ly < y < ry:
                    board[x][y] = 0
                elif board[x][y] != 0:
                    board[x][y] = 1
    
    q = deque([(characterX * 2, characterY * 2, 0)])
    
    while q:
        x, y, d = q.popleft()
        
        if x == itemX * 2 and y == itemY * 2:
            return d // 2
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            
            if board[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny, d + 1))
                visited[nx][ny] = True
