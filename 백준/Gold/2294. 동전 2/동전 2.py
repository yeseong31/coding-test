import sys
input = sys.stdin.readline


n, k = map(int, input().split())
dp = [100001] * (k + 1)
dp[0] = 0

for x in sorted([int(input().rstrip()) for _ in range(n)]):
    for i in range(x, k + 1):
        dp[i] = min(dp[i], dp[i - x] + 1)
print(dp[k] if dp[k] != 100001 else -1)