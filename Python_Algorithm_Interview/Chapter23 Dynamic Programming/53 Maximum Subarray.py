# 합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

        # 카데인 알고리즘
        # 각 단계마다 최댓값을 담아 어디서 끝나는지를 찾는 문제로 치환 -> O(n)
        # answer = -sys.maxsize
        # cur_sum = 0
        # for n in nums:
        #     cur_sum = max(n, cur_sum + n)
        #     answer = max(answer, cur_sum)
        # return answer


solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.maxSubArray(nums))
