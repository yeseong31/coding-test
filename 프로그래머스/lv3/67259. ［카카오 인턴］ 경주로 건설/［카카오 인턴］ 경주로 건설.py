from collections import deque
from copy import deepcopy


def solution(board):
    def bfs(a, b, d, c):
        q = deque([(a, b, d, c)])
        visited = [[False] * n for _ in range(n)]
        graph = deepcopy(board)
        
        while q:
            x, y, d, c = q.popleft()
            
            for nd in range(4):
                nx, ny = x + dx[nd], y + dy[nd]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == -1:
                    continue
                
                nc = c + (100 if d == nd else 600)
                if 0 < graph[nx][ny] <= nc:
                    continue
                
                graph[nx][ny] = nc
                q.append((nx, ny, nd, nc))
    
        return graph[n - 1][n - 1]
    
    n = len(board)
    dx, dy = (0, 1, 0, -1), (1, 0, -1 , 0)
    return min(bfs(0, 0, 0, 0), bfs(0, 0, 1, 0))
