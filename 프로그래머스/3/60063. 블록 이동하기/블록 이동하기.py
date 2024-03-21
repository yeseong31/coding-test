from collections import deque


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            new_board[i][j] = board[i - 1][j - 1]
    
    dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
    pos = ((1, 1), (1, 2))
    
    q = deque([(pos, 0)])
    visited = {pos,}
    
    while q:
        pos, cnt = q.popleft()
        if (n, n) in pos:
            return cnt
        
        result = []
        x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
        
        for i in range(4):
            nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
            
            if new_board[nx1][ny1] == 0 and new_board[nx2][ny2] == 0:
                result.append(((nx1, ny1), (nx2, ny2)))
        
        for i in (-1, 1):
            if x1 == x2 and new_board[x1 + i][y1] == new_board[x2 + i][y2] == 0:
                result.append(((x1, y1), (x1 + i, y1)))
                result.append(((x2, y2), (x2 + i, y2)))
                
            elif y1 == y2 and new_board[x1][y1 + i] == new_board[x2][y2 + i] == 0:
                result.append(((x1, y1), (x1, y1 + i)))
                result.append(((x2, y2), (x2, y2 + i)))
        
        for n_pos in result:
            if n_pos not in visited:
                visited.add(n_pos)
                q.append((n_pos, cnt + 1))
                
    return 0