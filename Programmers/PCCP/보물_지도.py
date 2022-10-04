from collections import deque


def solution(n, m, hole):
    answer = 1000001
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    board = [[0] * m for _ in range(n)]
    for a, b in hole:
        board[a - 1][b - 1] = -1
    visited = [['0'] * m for _ in range(n)]

    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = '1'

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != -1 and visited[nx][ny] != '1':
                board[nx][ny] = dist + 1
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = '1'

    if visited[n - 1][m - 1] == '1':
        answer = min(answer, board[n - 1][m - 1])

    q.append((n - 1, m - 1, 0))
    visited[n - 1][m - 1] = '2'

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == '2':
                continue
            elif board[nx][ny] == -1:
                nnx, nny = nx + dx[i], ny + dy[i]
                if 0 <= nnx < n and 0 <= nny < m and visited[nnx][nny] == '1':
                    answer = min(answer, board[nnx][nny] + dist + 1)
            else:
                board[nx][ny] = dist + 1
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = '2'

    if answer == 1000001:
        return -1
    return answer


print(solution(4, 4, [[2, 3], [3, 3]]))
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
