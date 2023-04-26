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