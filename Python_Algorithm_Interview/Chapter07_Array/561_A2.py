# 풀이 2 - 짝수 번째 값 계산

def arrayPairSum(nums: list[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum
