from collections import deque


def solution(maps):
    answer = 10001
    n, m = len(maps), len(maps[0])
    dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque([(0, 0, 1)])
    while q:
        x, y, d = q.popleft()
        if (x, y) == (n - 1, m - 1):
            answer = min(answer, d)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0 or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            q.append((nx, ny, d + 1))
    return answer if answer < 10001 else -1