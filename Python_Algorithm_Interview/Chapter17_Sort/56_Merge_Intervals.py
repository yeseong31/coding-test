"""
구간 병합(497p)
겹치는 구간을 병합하라
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []

        for x in sorted(intervals, key=lambda x: x[0]):
            if answer and answer[-1][1] >= x[0]:
                answer[-1][1] = max(answer[-1][1], x[1])
                continue
            answer.append(x)
        return answer


solution = Solution().merge

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution(intervals))  # [[1,6],[8,10],[15,18]]
