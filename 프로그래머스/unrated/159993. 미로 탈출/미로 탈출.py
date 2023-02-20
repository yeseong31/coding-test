from collections import deque


def solution(maps):
    def bfs(s, e):
        x, y = points[s]
        q = deque([(x, y, 0)])
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        visited[x][y] = True
        while q:
            x, y, d = q.popleft()
            if maps[x][y] == e:
                return d
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or visited[nx][ny] or maps[nx][ny] == 'X':
                    continue
                visited[nx][ny] = True
                q.append((nx, ny, d + 1))
        return 0
    
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    points = {}
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] in ('S', 'E', 'L'):
                points[maps[i][j]] = (i, j)
                
    s_to_l, l_to_e = bfs('S', 'L'), bfs('L', 'E')
    return s_to_l + l_to_e if s_to_l and l_to_e else -1