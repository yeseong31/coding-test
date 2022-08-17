"""
퇴사(377p)
"""


n = int(input())
t, p = [], []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
d = p + [0]
for i in range(n - 1, -1, -1):
    if i + t[i] > n:
        d[i] = d[i + 1]
    else:
        d[i] = max(d[i + 1], d[i + t[i]] + p[i])
print(d[0])
