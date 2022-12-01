import sys
input = sys.stdin.readline


def dfs(check, area):
    global answer
    if check == len(cctvs):
        answer = min(answer, sum([x.count('0') for x in area]))
        return

    x, y, cctv = cctvs[check]
    for direction in mode[cctv - 1]:
        lst = []
        for d in direction:
            nx, ny = x, y
            
            while True:
                nx, ny = nx + dx[d], ny + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or area[nx][ny] == '6':
                    break
                if area[nx][ny] != '0':
                    continue
                area[nx][ny] = '#'
                lst.append((nx, ny))

        dfs(check + 1, area)
        for a, b in lst:
            area[a][b] = '0'


dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

mode = [
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 3], [0, 1], [1, 2], [2, 3]],
    [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]],
    [[0, 1, 2, 3]]
]

n, m = map(int, input().split())
office, cctvs = [], []

for i in range(n):
    row = list(map(str, input().split()))
    for j, v in enumerate(row):
        if v not in ('0', '6'):
            cctvs.append((i, j, int(v)))
    office.append(row)

answer = 65
dfs(0, office)
print(answer)