import collections
import sys

input = sys.stdin.readline

# 시험관 크기 n, 바이러스의 종류 k
n, k = map(int, input().split())

# 바이러스
data = []

# 시험관의 정보
test_tube = []
for i in range(n):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        if r != 0:
            data.append((r, 0, i, j))
    test_tube.append(row)

# 큐
data.sort()
q = collections.deque(data)

# s초 뒤에 (x, y)에 존재하는 바이러스의 종류를 출력
s, x, y = map(int, input().split())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 매 초마다 큐에서 바이러스를 꺼내어 확산 후 다시 큐에 삽입, 반복
while q:
    virus, now, a, b = q.popleft()
    if now == s:
        break
    # 바이러스 확산
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        # 상하좌우로 이동할 수 없으면 패스
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 상하좌우에 0이 있거나 현재 바이러스의 우선순위가 더 높은 경우 이동
        if test_tube[nx][ny] == 0:
            test_tube[nx][ny] = virus
            q.append((virus, now + 1, nx, ny))

print(test_tube[x - 1][y - 1])