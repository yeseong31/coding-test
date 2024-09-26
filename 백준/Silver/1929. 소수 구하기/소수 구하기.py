m, n = map(int, input().split())
d = [True for _ in range(n + 1)]
d[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if d[i]:
        j = 2
        while i * j <= n:
            d[i * j] = False
            j += 1

for i in range(m, n + 1):
    if d[i]:
        print(i)