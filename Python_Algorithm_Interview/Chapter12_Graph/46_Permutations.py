# 순열(341p)
from itertools import permutations


def permute(nums: list[int]) -> list[list[int]]:
    return list(map(list, permutations(nums)))


nums = [1, 2, 3]
print(permute(nums))