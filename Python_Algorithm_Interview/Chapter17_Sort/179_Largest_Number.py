"""
가장 큰수(504p)
항목들을 조합하여 마들 수 있는 가장 큰 수를 출력하라.
"""
from typing import List


def largestNumber(nums: List[int]) -> str:
    i = 1
    nums = list(map(str, nums))
    while i < len(nums):
        j = i
        while j > 0 and nums[j - 1] + nums[j] < nums[j] + nums[j - 1]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
        i += 1
    return str(int(''.join(nums)))


nums = [10, 2]
print(largestNumber(nums))

nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))

nums = [111311, 1113]
print(largestNumber(nums))

# 0 붙어 있는 아이는 맨 뒤로
# 나머지는 앞으로
