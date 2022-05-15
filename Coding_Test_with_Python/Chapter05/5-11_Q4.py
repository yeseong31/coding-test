# 실전 문제 - 미로 탈출(152p)

from collections import deque

n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0


# 너비 탐색
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 사방을 살펴 이동 가능한 좌표 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 만약 이동할 위치가 범위를 벗어나면
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 만약 이동할 위치가 0이라면
            if miro[nx][ny] == 0:
                continue
            # 만약 이동할 위치가 1이라면
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
    return miro[n - 1][m - 1]


# 현재 위치(1, 1) -> 실제 2차원 리스트 위치는 (0, 0)
print(bfs(0, 0))
