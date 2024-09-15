m = int(input())
n = int(input())
prime = []
for i in range(m, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
        if cnt > 2:
            break
    if cnt == 2:
        prime.append(i)
if len(prime) != 0: print(sum(prime))
print(prime[0] if len(prime) != 0 else -1)