# 풀이 3 - 첫 번째 수를 뺀 결과 키 조회

def twoSum(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
