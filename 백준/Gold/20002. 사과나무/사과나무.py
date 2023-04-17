n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + board[i][j]

answer = -1001
for k in range(n, 0, -1):
    for i in range(n, k - 1, -1):
        for j in range(n, k - 1, -1):
            answer = max(answer, dp[i][j] + dp[i - k][j - k] - dp[i][j - k] - dp[i - k][j])
print(answer)
