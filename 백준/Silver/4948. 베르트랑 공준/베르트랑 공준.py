x = 123456 * 2 + 1
prime = [True] * x

for i in range(2, int(x * 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, x, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if prime[i]:
            count += 1
    print(count)