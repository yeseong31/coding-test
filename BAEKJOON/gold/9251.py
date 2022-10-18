# LCS

# 풀이 1 (30840KB, 268ms)
a = input()
b = input()
n, m = len(a), len(b)
lcs = [0] * m

for i in range(n):
    cnt = 0
    for j in range(m):
        if cnt < lcs[j]:
            cnt = lcs[j]
        elif a[i] == b[j]:
            lcs[j] = cnt + 1
print(max(lcs))

# 풀이 2 (55032KB, 668ms)
# a = input()
# b = input()
# n, m = len(a), len(b)
# lcs = [[0] * (m + 1) for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if a[i - 1] == b[j - 1]:
#             lcs[i][j] = lcs[i - 1][j - 1] + 1
#         else:
#             lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
# print(lcs[n][m])
