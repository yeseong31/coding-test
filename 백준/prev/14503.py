# 로봇 청소기
# https://www.acmicpc.net/problem/14503

n, m = map(int, input().split())
r, c, d = map(int, input().split())

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[r][c] = True
answer = 1

while True:
    check = False
    for _ in range(4):
        nr, nc = r + dr[(d + 3) % 4], c + dc[(d + 3) % 4]
        d = (d + 3) % 4
        if nr < 0 or nr >= n or nc < 0 or nc >= m or board[nr][nc] == 1 or visited[nr][nc]:
            continue
        visited[nr][nc] = True
        answer += 1
        r, c = nr, nc
        check = True
        break
    if not check:
        if board[r - dr[d]][c - dc[d]] == 1:
            print(answer)
            break
        else:
            r, c = r - dr[d], c - dc[d]
