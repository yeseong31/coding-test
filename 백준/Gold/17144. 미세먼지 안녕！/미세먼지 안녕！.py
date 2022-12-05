import sys
input = sys.stdin.readline


def spread():
    check = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] in (0, -1):
                continue
            tmp = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or board[nx][ny] == -1:
                    continue
                check[nx][ny] += board[x][y] // 5
                tmp += board[x][y] // 5
            board[x][y] -= tmp
    
    for i in range(r):
        for j in range(c):
            board[i][j] += check[i][j]
            
            
def rotate_top(x):
    # 왼쪽 줄
    for i in range(x - 1, 0, -1):
        board[i][0], board[i - 1][0] = board[i - 1][0], board[i][0]
    # 윗줄
    for j in range(c - 1):
        board[0][j], board[0][j + 1] = board[0][j + 1], board[0][j]
    # 오른쪽 줄
    for i in range(x):
        board[i][-1], board[i + 1][-1] = board[i + 1][-1], board[i][-1]
    # 아랫줄
    for j in range(c - 1, 1, -1):
        board[x][j - 1], board[x][j] = board[x][j], board[x][j - 1]


def rotate_bottom(x):
    # 왼쪽 줄
    for i in range(x + 1, r - 1):
        board[i][0], board[i + 1][0] = board[i + 1][0], board[i][0]
    # 아랫줄
    for j in range(c - 1):
        board[-1][j], board[-1][j + 1] = board[-1][j + 1], board[-1][j]
    # 오른쪽 줄
    for i in range(r - 1, x, -1):
        board[i][-1], board[i - 1][-1] = board[i - 1][-1], board[i][-1]
    # 윗줄
    for j in range(c - 1, 1, -1):
        board[x][j], board[x][j - 1] = board[x][j - 1], board[x][j]


r, c, t = map(int, input().split())

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

board = [list(map(int, input().split())) for _ in range(r)]
a = -1  # 공기청정기 좌표(상단)

for x in range(r):
    if board[x][0] == -1:
        a = x
        break
    
for _ in range(t):
    spread()
    rotate_top(a)
    rotate_bottom(a + 1)
    # 공기 정화
    board[a][1] = board[a + 1][1] = 0
    
print(sum(sum(b) for b in board) + 2)
