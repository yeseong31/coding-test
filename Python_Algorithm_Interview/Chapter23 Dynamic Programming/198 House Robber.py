# 어느 집에서든 돈을 훔쳐올 수 있지만 바로 옆집은 훔칠 수 없고 한 칸 이상 떨어진 집만 가능하다.
# 각 집에는 훔칠 수 있는 돈의 액수가 입력값으로 표기되어 있다.
# 훔칠 수 있는 가장 큰 금액을 출력하라.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        d = [0] * n
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])

        for i in range(2, n):
            d[i] = max(d[i - 2] + nums[i], d[i - 1])
        return max(d[n - 2], d[n - 1])


solution = Solution()

nums = [6,3,10,8,2,10,3,5,10,5,3]
print(solution.rob(nums))

nums = [2, 7, 9, 3, 1]
print(solution.rob(nums))
