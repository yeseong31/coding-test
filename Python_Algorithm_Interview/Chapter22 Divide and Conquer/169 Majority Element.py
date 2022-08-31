# 과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라.
from collections import Counter, defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 풀이 1: 394ms ------------------------------
        # return Counter(nums).most_common()[0][0]

        # 풀이 2: 423 ms ------------------------------
        # cnt = defaultdict(int)
        # for n in nums:
        #     cnt[n] += 1
        #     if cnt[n] > len(nums) // 2:
        #         return n

        # 풀이 3: 265 ms ------------------------------
        # cnt = defaultdict(int)
        # for n in nums:
        #     if cnt[n] == 0:
        #         cnt[n] = nums.count(n)
        #     if cnt[n] > len(nums) // 2:
        #         return n

        # 풀이 4: 220 ms ------------------------------
        # return sorted(nums)[len(nums) // 2]

        # 풀이 5: 527 ms ------------------------------
        length = len(nums)
        if length == 1:
            return nums[0]
        # 분할
        a = self.majorityElement(nums[:length // 2])
        b = self.majorityElement(nums[length // 2:])
        # 정복
        # if nums.count(a) > length // 2:
        #     return a
        # return b
        return [b, a][nums.count(a) > length // 2]



solution = Solution()

nums = [3, 2, 3]
print(solution.majorityElement(nums))
