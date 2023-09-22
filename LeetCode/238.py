from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        target = 1
        for v in nums:
            target *= v
        
        result = []
        
        p = 1
        for v in nums:
            result.append(p)
            p *= v
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= p
            p *= nums[i]
        
        return result
