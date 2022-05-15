# 실전 문제 - 효율적인 화폐 구성(226p)

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(data[i], m + 1):
        d[j] = min(d[j], d[j - data[i]] + 1)

if d[m] != 10001:
    print(d[m])
else:
    print(-1)
