from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


# from bisect import bisect_left, bisect_right
#
# class Solution:
# def search(self, nums: List[int], target: int) -> int:
#     left = bisect_left(nums, target)
#     if left < len(nums) and nums[left] == target:
#         return left
#     return -1
