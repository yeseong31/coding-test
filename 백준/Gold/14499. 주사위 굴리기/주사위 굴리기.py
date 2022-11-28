TOP = 1
BOTTOM = 3

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [0] * 6
dice[BOTTOM] = board[x][y]

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

for i in list(map(int, input().split())):
    nx, ny = x + dx[i - 1], y + dy[i - 1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    a, b, c, d, e, f = dice
    if i == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = a, f, c, e, b, d
    elif i == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = a, e, c, f, d, b
    elif i == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, c, d, a, e, f
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, a, b, c, e, f
    
    x, y = nx, ny
    if board[x][y] == 0:
        board[x][y] = dice[BOTTOM]
    else:
        dice[BOTTOM] = board[x][y]
        board[x][y] = 0
    print(dice[TOP])
