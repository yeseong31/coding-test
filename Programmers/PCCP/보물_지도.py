from collections import deque


def solution(n, m, hole):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    board = [[1000001] * m for _ in range(n)]
    for a, b in hole:
        board[a - 1][b - 1] = -1

    q = deque()
    q.append((0, 0, True))
    board[0][0] = 0

    while q:
        x, y, jump = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위를 넘어선 경우는 탐색하지 않음
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우
            elif board[nx][ny] == -1:
                # 점프를 이미 쓴 경우에는 탐색하지 않음
                if not jump:
                    continue
                nnx, nny = nx + dx[i], ny + dy[i]
                # 점프 이후의 칸이 범위를 넘어서거나 벽인 경우에도 탐색하지 않음
                if nnx < 0 or nnx >= n or nny < 0 or nny >= m or board[nnx][nny] == -1:
                    continue
                # 점프 이후의 칸의 거리를 갱신할 수 있는 경우 갱신
                elif board[nnx][nny] > board[x][y] + 1:
                    board[nnx][nny] = board[x][y] + 1
                    q.append((nnx, nny, False))
            # 이동 후 칸의 거리를 갱신할 수 있는 경우 갱신
            elif board[nx][ny] > board[x][y] + 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny, jump))

    if board[n - 1][m - 1] == 1000001:
        return -1
    return board[n - 1][m - 1]


print(solution(4, 4, [[1, 3], [2, 3], [3, 3], [2, 4]]))
print(solution(5, 4, [[2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
