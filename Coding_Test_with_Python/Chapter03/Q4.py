
# 예제 3-4 1이 될 때까지(99p)

n, k = map(int, input().split())
count = 0

while n > 1:
    if n % k != 0:
        count += n % k
        n -= n % k
    if n == 0:
        count -= 1
        break
    n //= k
    count += 1

print(count)
