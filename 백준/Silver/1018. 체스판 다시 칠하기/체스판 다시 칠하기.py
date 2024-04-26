# 체스판 다시 칠하기

# 체스판을 색칠하는 경우
# 1) 맨 왼쪽 위 칸이 흰색인 경우
# 2) 맨 왼쪽 위 칸이 검은색인 경우


def check(i, j):
    white = 0
    black = 0
    for x in range(i, i + 8):
        for y in range(j, j + 8):
            if (x + y) % 2 == 0:
                if board[x][y] != 'W':
                    white += 1
                if board[x][y] != 'B':
                    black += 1
            else:
                if board[x][y] != 'B':
                    white += 1
                if board[x][y] != 'W':
                    black += 1
    res.append(white)
    res.append(black)


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

res = []

for a in range(n - 7):
    for b in range(m - 7):
        check(a, b)

print(min(res))
