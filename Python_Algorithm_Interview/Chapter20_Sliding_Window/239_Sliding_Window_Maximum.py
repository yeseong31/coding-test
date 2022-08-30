# 배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝가지 이동하면서 최대 슬라이딩 윈도우를 구하라.
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 결괏값
        answer = []
        # 슬라이딩 윈도우(인덱스 값 저장)
        q = collections.deque()

        for i, v in enumerate(nums):
            # 윈도우 사이즈는 k로 고정
            if q and i - q[0] == k:
                q.popleft()
            # 현재 값보다 작은 원소는 저장하지 않음
            while q and v > nums[q[-1]]:
                q.pop()
            # 최댓값(인덱스) 갱신
            q.append(i)
            # 결괏값 갱신
            if i >= k - 1:
                answer.append(nums[q[0]])

        return answer


# 시간 초과
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


solution = Solution()

nums = [7,2,4]
k = 2
print(solution.maxSlidingWindow(nums, k))
