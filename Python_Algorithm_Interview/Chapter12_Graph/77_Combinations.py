# 조합(346p)
from itertools import combinations


def combine(n: int, k: int) -> list[list[int]]:
    return list(map(list, combinations(range(1, n + 1), k)))
