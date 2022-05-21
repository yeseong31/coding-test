import collections


def bfs(x, y):
    q = collections.deque()
    q.append((x, y))
    board[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 0:
                continue
            board[nx][ny] = 0
            q.append((nx, ny))
            cnt += 1
    return cnt


# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
# 지도
board = []
for _ in range(n):
    board.append(list(map(int, input())))

result = []

# bfs 수행
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            result.append(bfs(i, j))

# 결과 출력
print(len(result))
for r in sorted(result):
    print(r)
