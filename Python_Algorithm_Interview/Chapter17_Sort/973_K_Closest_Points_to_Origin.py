"""
원점에 K번째로 가까운 점(511p)
평면상에 points 목록이 있을 때,
원점에서 K번 가까운 점 목록을 순서대로 출력하라
이때 평면상 두 점의 거리는 유클리드 거리로 한다.
"""
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: (x[0]**2+x[1]**2))[:k]


# 또 다른 풀이
# lass Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         q = []
#         for a, b in points:
#             heapq.heappush(q, (-(a**2 + b**2), a, b))
#         return [[a, b] for _, a, b in heapq.nlargest(k, q)]


sol = Solution()
points = [[1,3],[-2,2]]
k = 1
print(sol.kClosest(points, k))

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(sol.kClosest(points, k))
