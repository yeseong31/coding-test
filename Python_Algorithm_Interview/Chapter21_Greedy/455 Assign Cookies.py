# 아이들에게 1개씩 쿠키를 나눠줘야 한다.
# 각 아이 child_i마다 '그리드 팩터 g[i]'를 가지고 있으며, 이는 아이가 만족하는 최소 쿠키의 크기를 말한다.
# 각 쿠키 cookie_j는 크기 s[j]를 가지고 있으며, s[j] >= g[i]이어야 아이가 만족하며 쿠키를 받는다.
# 최대 몇 명의 아이들에게 쿠키를 줄 수 있는지 출력하라.
import bisect
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g: 아이들, s: 쿠키
        g.sort()
        s.sort()

        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i

    # 다른 풀이
    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        answer = 0
        for i in s:
            # 이진 검색으로 더 큰 인덱스 탐색
            idx = bisect.bisect_right(g, i)
            if idx > answer:
                answer += 1
        return answer


solution = Solution()

g = [1, 2, 3]
s = [1, 1]
print(solution.findContentChildren(g, s))
