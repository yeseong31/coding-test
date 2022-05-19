'''
215. 배열의 K번째 큰 요소(456p)

정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
'''
import heapq
from typing import List


class Solution:
    # k번째 큰 값 추출
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    # k번째 작은 값 추출
    def findKthSmallest(self, nums: List[int], k: int) -> int:
        return heapq.nsmallest(k, nums)[-1]

# 풀이 2 --------------------------------------------------------
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heapq.heapify(nums)  # 중간에 값을 추가하는 형태가 아니므로 heapify()로 한 번에 처리
#
#         # k번째 큰 요소 == len(nums) - k번째 작은 요소
#         for _ in range(len(nums) - k):
#             heapq.heappop(nums)
#
#         return heapq.heappop(nums)

# 풀이 1 --------------------------------------------------------
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         q = []
#         for n in nums:
#             heapq.heappush(q, -n)
#
#         answer = 0
#         while q and k > 0:
#             answer = heapq.heappop(q)
#             k -= 1
#
#         return -answer


solution = Solution().findKthLargest

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(solution(nums, k))  # 5
