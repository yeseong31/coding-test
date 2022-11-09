n = int(input())
lst = list(map(int, input().split()))

board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if lst[i - 1] == lst[n - j]:
            board[i][j] = board[i - 1][j - 1] + 1
        else:
            board[i][j] = max(board[i - 1][j], board[i][j - 1])

print(n - board[n][n])