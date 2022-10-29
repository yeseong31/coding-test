import sys
input = sys.stdin.readline

answer = 0
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

q = set()
q.add((0, 0, board[0][0]))

while q:
    x, y, alpha = q.pop()
    answer = max(answer, len(alpha))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or board[nx][ny] in alpha:
            continue
        q.add((nx, ny, alpha + board[nx][ny]))

print(answer)