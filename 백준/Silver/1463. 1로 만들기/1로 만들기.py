import sys
input = sys.stdin.readline

x = int(input())

d = [0] * (x + 1)

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    for j in [2, 3]:
        if i % j == 0:
            d[i] = min(d[i], d[i // j] + 1)

print(d[x])