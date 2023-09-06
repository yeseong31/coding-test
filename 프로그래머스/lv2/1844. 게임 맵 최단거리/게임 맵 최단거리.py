from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    q = deque([(0, 0, 1)])
    
    while q:
        x, y, d = q.popleft()
        if (x, y) == (n - 1, m - 1):
            return d
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0 or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            q.append((nx, ny, d + 1))
    
    return -1