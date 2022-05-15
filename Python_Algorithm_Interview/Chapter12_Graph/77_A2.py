# 풀이 2 - itertools 모듈 사용
from itertools import combinations


def combine(n: int, k: int) -> list[list[int]]:
    return list(map(list, combinations(range(1, n + 1), k)))
