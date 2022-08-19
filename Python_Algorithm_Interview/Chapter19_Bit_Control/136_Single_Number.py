from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        # XOR: 입력값이 서로 다르면 True, 서로 동일하면 False
        for n in nums:
            answer ^= n
        return answer
