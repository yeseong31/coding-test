def solution():
    n = int(input())
    dice = list(map(int, input().split()))

    if n == 1:
        return sum(dice) - max(dice)

    mul = [4, 8 * n - 12, 5 * (n ** 2) - 16 * n + 12]
    comb_3 = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]
    comb_2 = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    result = [min(dice[a] + dice[b] + dice[c] for a, b, c in comb_3),
              min(dice[a] + dice[b] for a, b in comb_2),
              min(dice)]

    return sum(x * y for x, y in zip(mul, result))


print(solution())