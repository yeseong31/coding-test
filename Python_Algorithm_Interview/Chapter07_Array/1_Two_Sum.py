# 두 수의 합(173p)
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
import collections
from itertools import combinations


def twoSum(nums:list[int], target:int) -> list[int]:
    nums_map = {}

    # 키와 값을 바꾸어서 dict에 저장
    for i, n in enumerate(nums):
        nums_map[n] = i

    # target에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, n in enumerate(nums):
        if target - n in nums_map and i != nums_map[target - n]:
            return [i, nums_map[target - n]]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
# Output: [0, 1]

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))

nums = [3, 3]
target = 6
print(twoSum(nums, target))
