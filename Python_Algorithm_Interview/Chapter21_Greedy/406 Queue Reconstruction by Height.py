# 여러 명의 사람들이 줄을 서 있다.
# 각각의 사람은 (h, k)의 두 정수 쌍을 갖는데,
# h는 그 사람의 키, k는 앞에 줄 서 있는 사람들 중 자신의 키 이상인 사람들의 수를 뜻한다.
# 이 값이 올바르도록 줄을 재정렬하는 알고리즘을 작성하라.
import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 결괏값
        answer = []

        # 키 큰 사람부터 삽입
        for t, n in sorted(people, key=lambda x: (-x[0], x[1])):
            answer.insert(n, [t, n])

        return answer

    # 다른 풀이: 우선순위 큐 이용 (100ms 정도 더 빠름)
    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        q = []
        for t, n in people:
            heapq.heappush(q, (-t, n))

        answer = []
        while q:
            t, n = heapq.heappop(q)
            answer.insert(n, [-t, n])
        return answer


solution = Solution()

people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(solution.reconstructQueue(people))

people = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
print(solution.reconstructQueue(people))
