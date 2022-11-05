MAX_SIZE = int(1e7)


def is_prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


a, b = map(int, input().split())
if b > MAX_SIZE:
    b = MAX_SIZE
if a % 2 == 0:
    a += 1

answer = [n for n in range(a, b + 1, 2) if str(n) == str(n)[::-1]]
answer = [n for n in answer if is_prime_number(n)]
for x in answer:
    print(x)
print(-1)
