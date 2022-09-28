import collections


def bfs(x, y, h, v):
    q = collections.deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        x, y = q.popleft()
        # 상하좌우 체크
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 범위 밖이거나 물에 잠긴 지역이라면
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if v[nx][ny] == 0 and board[nx][ny] > h:
                v[nx][ny] = 1
                q.append((nx, ny))


n = int(input())

# 해당 지역의 최대 높이
max_height = 0
# 확인할 지역
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    max_height = max(max_height, max(row))

# 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0
# 물에 잠기는 영역의 수를 '물 높이'에 따라 체크
for height in range(max_height + 1):
    tmp = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 물에 잠기지 않은 영역에 한하여 bfs 탐색
            if visited[i][j] == 0 and board[i][j] > height:
                bfs(i, j, height, visited)
                tmp += 1
    result = max(result, tmp)

print(result)
