from math import gcd


def find_divisors(x):
    answer = []
    for i in range(2, int(x ** 0.5) + 1):
        div, mod = divmod(x, i)
        if mod == 0:
            answer.append(i)
            answer.append(div)
    answer.append(x)
    return sorted(list(set(answer)))


n = int(input())
numbers = sorted([int(input()) for _ in range(n)])

# A - B, B - C, ...
diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

prev = diffs[0]
for j in range(1, len(diffs)):
    prev = gcd(prev, diffs[j])

result = find_divisors(prev)
print(*result)
