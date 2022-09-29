# 편집 거리(382p)

a = input()
b = input()

n, m = len(a), len(b)

# 2차원 dp 테이블
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = i
for j in range(m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 두 문자가 같은 경우
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        # 두 문자가 다를 경우
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

print(dp[n - 1][m - 1])
