from collections import deque


def solution(board):
    answer = int(1e9)

    # 보드의 크기
    n = len(board)
    # 방향
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    # DP
    dp = [[[answer] * n for _ in range(n)] for _ in range(4)]
    # BFS
    q = deque()
    q.append((0, 0, 0, 0))
    q.append((0, 0, 0, 1))

    while q:
        # 좌표 (x, y), 거리, 회전
        x, y, d, z = q.popleft()
        for i in range(4):
            nx, ny, nd = x + dx[i], y + dy[i], d + 100
            # 진행할 수 없는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
                continue
            # 회전에 따른 거리 계산
            if z != i:
                nd += 500
            # DP 테이블 갱신
            if dp[i][nx][ny] > nd:
                dp[i][nx][ny] = nd
                q.append((nx, ny, nd, i))

    for i in range(4):
        answer = min(answer, dp[i][n - 1][n - 1])
    return answer
