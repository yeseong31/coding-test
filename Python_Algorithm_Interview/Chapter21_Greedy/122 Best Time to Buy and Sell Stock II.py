# 여러 번의 거래로 낼 수 있는 최대 이익을 산출하라.
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 결괏값
        answer = 0
        # 시작점
        prev = prices[0]

        for cur in prices[1:]:
            if cur >= prev:
                answer += cur - prev
            prev = cur

        return answer

        # 다른 풀이
        # return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


solution = Solution()

prices = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices))
