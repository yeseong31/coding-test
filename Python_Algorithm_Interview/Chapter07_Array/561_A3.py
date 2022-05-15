# 풀이 3 = 파이썬다운 방식

def arrayPairSum(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])
