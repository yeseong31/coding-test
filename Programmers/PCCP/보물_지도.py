from collections import deque


# 정확성 36.6
def solution(n, m, hole):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    board = [[1000001] * m for _ in range(n)]
    for a, b in hole:
        board[a - 1][b - 1] = -1
    visited = [[False] * m for _ in range(n)]

    q = deque()
    q.append((0, 0, True))
    visited[0][0] = True
    board[0][0] = 0

    while q:
        x, y, jump = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m \
                    or (visited[nx][ny] and board[nx][ny] <= board[x][y] + 1):
                continue
            if board[nx][ny] == -1:
                if not jump:
                    continue
                nnx, nny = nx + dx[i], ny + dy[i]
                if nnx < 0 or nnx >= n or nny < 0 or nny >= m or board[nnx][nny] == -1 \
                        or (visited[nnx][nny] and board[nnx][nny] <= board[x][y] + 1):
                    continue
                q.append((nnx, nny, False))
                visited[nnx][nny] = True
                board[nnx][nny] = board[x][y] + 1
            else:
                q.append((nx, ny, jump))
                visited[nx][ny] = True
                board[nx][ny] = board[x][y] + 1

    for bo in board:
        print(bo)
    print()
    for vi in visited:
        print(vi)
    print()

    if not visited[n - 1][m - 1]:
        return -1
    return board[n - 1][m - 1]


print(solution(4, 4, [[2, 3], [3, 3]]))
print(solution(5, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [5, 1]]))
