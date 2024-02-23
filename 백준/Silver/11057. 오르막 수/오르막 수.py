dp = [1] * 10

for _ in range(int(input()) - 1):
    for x in range(1, 10):
        dp[x] += dp[x - 1]

print(sum(dp) % 10007)
