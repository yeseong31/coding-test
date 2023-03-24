from collections import deque


def solution(board):
    def bfs(x, y, d, c):
        q = deque([(x, y, d, c)])
        graph = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    graph[i][j] = -1

        while q:
            x, y, d, c = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == -1:
                    continue
                if i == d:
                    nc = c + 100
                else:
                    nc = c + 600
                if graph[nx][ny] == 0 or graph[nx][ny] > nc:
                    graph[nx][ny] = nc            
                    q.append((nx, ny, i, nc))
        return graph[n - 1][n - 1]
    
    n = len(board)
    dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
    return min(bfs(0, 0, 0, 0), bfs(0, 0, 1, 0))
