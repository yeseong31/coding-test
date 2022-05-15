# 실전 문제 - 음료수 얼려 먹기(149p)

# 가로 길이 N, 세로 길이 M
n, m = map(int, input().split())
# 얼음틀 data
data = []
for _ in range(n):
    data.append(list(map(int, input())))


def dfs(x, y):
    # 탐색 범위에서 벗어나면 False
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 그렇지 않다면 탐색을 해야 함
    # 현재 위치가 0이면 탐색 시작
    if data[x][y] == 0:
        # 사방으로 퍼져나가면서 탐색 시작
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        # 방문 처리
        data[x][y] = 1
        return True
    else:
        return False


count = 0
for i in range(n):
    for j in range(m):
        # 깊이 우선 탐색을 했을 때 값이 참이면 1 카운트
        if dfs(i, j):
            count += 1

print(count)
