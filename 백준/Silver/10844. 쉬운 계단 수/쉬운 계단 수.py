n = int(input())
dp = [0] + [1] * 9

for _ in range(n - 1):
    prev = dp[:]
    dp[0] = prev[1]

    for i in range(1, 9):
        dp[i] = prev[i - 1] + prev[i + 1]

    dp[9] = prev[8]

print(sum(dp) % 1_000_000_000)
