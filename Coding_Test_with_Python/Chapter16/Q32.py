"""
Q32 정수 삼각형(376p)
"""

# 삼각형의 크기 n
import copy

n = int(input())
# 정수 삼각형
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# dp 테이블
dp = copy.deepcopy(triangle)

for i in range(1, len(triangle)):
    for j in range(i + 1):
        # 상단
        top = 0 if j == i else dp[i - 1][j]
        # 왼쪽 상단
        left_top = 0 if j == 0 else dp[i - 1][j - 1]
        # 값 비교
        dp[i][j] += max(top, left_top)

print(max(dp[n - 1]))
