# 배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝가지 이동하면서 최대 슬라이딩 윈도우를 구하라.
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # 인덱스 값 삽입
        answer = []

        for i, v in enumerate(nums):
            # 윈도우 사이즈는 k로 고정
            if q and i - q[0] == k:
                q.popleft()
            # v보다 작은 값은 모두 삭제
            while q and v > nums[q[-1]]:
                q.pop()
            q.append(i)

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
