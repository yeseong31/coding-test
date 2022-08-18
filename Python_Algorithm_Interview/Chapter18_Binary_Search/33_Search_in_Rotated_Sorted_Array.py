from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = 0
        for i, n in enumerate(nums):
            if n == target:
                return i
            if nums[idx] > n:
                idx = i
                break
        nums = nums[idx:] + nums[:idx]
        left = bisect_left(nums, target)
        if left < len(nums) and nums[left] == target:
            return idx + left
        return -1


s = Solution()
print(s.search([3, 1], 3))
