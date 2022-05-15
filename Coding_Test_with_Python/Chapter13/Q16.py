"""
연구소 (341p)
"""
import collections
import copy
import sys

input = sys.stdin.readline


def bfs():
    q = collections.deque()
    virus_map = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            # 바이러스인 경우
            if virus_map[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + d[i]
            ny = y + d[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if virus_map[nx][ny] == 0:
                virus_map[nx][ny] = 2
                q.append((nx, ny))

    global answer
    cnt = 0
    for v in virus_map:
        cnt += v.count(0)
    answer = max(answer, cnt)


def createWall(w):
    if w == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            # 빈 칸인 경우
            if lab[i][j] == 0:
                # 벽 설치
                lab[i][j] = 1
                # 개수 +1
                createWall(w + 1)
                # 벽 제거
                lab[i][j] = 0


# 세로 크기 n, 가로 크기 m
n, m = map(int, input().split())
# 연구소 지도
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

# 상하좌우로 바이러스가 퍼질 예정
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = 0
createWall(0)
print(answer)
