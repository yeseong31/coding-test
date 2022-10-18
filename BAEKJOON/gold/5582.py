# 공통 부분 문자열

# PyPy3 풀이 (241040KB, 440ms)
import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

n, m = len(a), len(b)
lcs = [[0] * (m + 1) for _ in range(n + 1)]

answer = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
            answer = max(answer, lcs[i][j])
print(answer)
