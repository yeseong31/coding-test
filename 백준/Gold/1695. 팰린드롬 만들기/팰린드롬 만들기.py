import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

p, c = [], []
for i in range(n):
    pp, p, c = p, c, []  # double prev, prev, cur
    for j in range(n - i):
        if i == 0:
            c.append(0)
            continue
        if lst[j] != lst[i + j]:
            c.append(min(p[j], p[j + 1]) + 1)
            continue
        if i == 1:
            c.append(0)
            continue
        c.append(pp[j + 1])

print(c[0])