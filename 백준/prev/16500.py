# 문자열 판별

s = input()
n = int(input())
a = [input() for _ in range(n)]
dp = [0] * (len(s) + 1)
dp[len(s)] = 1

for pos in range(len(s) - 1, -1, -1):
    for j in range(n):
        if s.find(a[j], pos) == pos and dp[pos + len(a[j])] == 1:
            dp[pos] = 1
            break
        else:
            dp[pos] = 0

print(dp[0])
