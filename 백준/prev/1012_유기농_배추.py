import collections
import sys
input = sys.stdin.readline


def bfs(x, y):
    q = collections.deque()
    q.append((x, y))
    board[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 밖이거나 배추가 심어져 있지 않은 경우
            if nx < 0 or nx >= m or ny < 0 or ny >= n or board[nx][ny] == 0:
                continue
            board[nx][ny] = 0
            q.append((nx, ny))


# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 테스트 케이스의 수만큼 반복
for _ in range(int(input())):
    # 배추밭의 가로, 세로, 배추의 수
    m, n, k = map(int, input().split())
    # 배추밭
    board = [[0] * n for _ in range(m)]
    # 배추의 위치
    for _ in range(k):
        a, b = map(int, input().split())
        board[a][b] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
