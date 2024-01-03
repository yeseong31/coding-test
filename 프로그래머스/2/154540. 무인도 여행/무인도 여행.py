from collections import deque


def solution(maps: list):
    dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
    q = deque()
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    def bfs(x, y):
        q.append((x, y))
        visited[x][y] = True
        count = int(maps[x][y])
        
        while q:
            x, y = q.popleft()
            
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    count += int(maps[nx][ny])
                    q.append((nx, ny))
        
        return count
    
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))
        
    return sorted(answer) if answer else [-1]
