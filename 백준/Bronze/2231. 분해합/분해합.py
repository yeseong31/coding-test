n = int(input())
INF = int(1e9)

for i in range(1, n + 1):
    m = i + sum(map(int, str(i)))
    if m == n:
        print(i)
        break
    if i == n:
        print(0)