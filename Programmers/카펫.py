def solution(brown, yellow):
    n = brown + yellow
    for i in range(3, int(n ** 0.5) + 1):
        if n % i != 0:
            continue
        x, y = n // i, i
        if yellow == (x - 2) * (y - 2):
            return [x, y]


brown = [10, 8, 24]
yellow = [2, 1, 24]
for b, y in zip(brown, yellow):
    print(solution(b, y))
