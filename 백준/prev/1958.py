# LCS 3
import sys
input = sys.stdin.readline

a, b, c = [input().strip() for _ in range(3)]
p, q, r = len(a), len(b), len(c)
lcs = [[[0] * (r + 1) for _ in range(q + 1)] for _ in range(p + 1)]

for i in range(1, p + 1):
    for j in range(1, q + 1):
        for k in range(1, r + 1):
            if a[i - 1] == b[j - 1] == c[k - 1]:
                lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
            else:
                lcs[i][j][k] = max(lcs[i - 1][j][k], lcs[i][j - 1][k], lcs[i][j][k - 1])

answer = -1
for i in range(1, p + 1):
    for j in range(1, q + 1):
        answer = max(answer, max(lcs[i][j]))
print(answer)
