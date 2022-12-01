import sys

input = sys.stdin.readline


def watch_area(a, b, direction, board):
    xy = []
    for d in direction:
        x, y = a, b

        while True:
            x, y = x + dx[d], y + dy[d]
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] == '6':
                break

            if board[x][y] == '0':
                board[x][y] = '#'
                xy.append((x, y))
    return xy


def dfs(check, area):
    global answer

    if check == len(cctvs):
        answer = min(answer, sum([x.count('0') for x in area]))
        return

    x, y, cctv = cctvs[check]
    for i in mode[cctv - 1]:
        lst = watch_area(x, y, i, area)
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
        if v in ['0', '6']:
            continue
        cctvs.append((i, j, int(v)))
    office.append(row)

answer = 65
dfs(0, office)
print(answer)
