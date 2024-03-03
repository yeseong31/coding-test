from collections import deque


def solution(land):
    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = True
        left, right = m, 0
        result = 1

        while q:
            x, y = q.popleft()
            left, right = min(y, left), max(y, right)

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m or land[nx][ny] == 0 or visited[nx][ny]:
                    continue

                result += 1
                visited[nx][ny] = True
                q.append((nx, ny))

        for i in range(left, right + 1):
            answer[i] += result

    dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
    
    n, m = len(land), len(land[0])
    answer = [0] * m
    
    visited = [[False] * m for _ in range(n)]

    for j in range(m):
        for i in range(n):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    return max(answer)
