def solution(n):
    if n % 2 == 1:
        return 0
    if n == 2:
        return 3
    if n == 4:
        return 11

    d = [0] * (n + 1)
    d[2] = 3
    d[4] = 11

    for i in range(6, n + 1, 2):
        d[i] = 3 * d[i - 2] + 2 * sum(d[2:i - 2]) + 2
    return d[n]


print(solution(int(input())))
