# 풀이 2 - itertools 모듈 사용
from itertools import permutations


def permute(nums: list[int]) -> list[list[int]]:
    return list(map(list, permutations(nums)))