# 풀이 4 - 조회 구조 개선

def twoSum(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))

nums = [3, 3]
target = 6
print(twoSum(nums, target))
