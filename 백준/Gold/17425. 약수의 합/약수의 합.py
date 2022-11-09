import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
mx = max(numbers)
dp = [1] * (mx + 1)

for i in range(2, mx + 1):
    j = i
    while j <= mx:
        dp[j] += i
        j += i

for i in range(2, mx + 1):
    dp[i] += dp[i - 1]

for x in numbers:
    print(dp[x])
