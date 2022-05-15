x = int(input())

d = [0] * 30001
num = [2, 3, 5]

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    for j in num:
        if i % j == 0:
            d[i] = min(d[i], d[i // j] + 1)

print(d[x])
