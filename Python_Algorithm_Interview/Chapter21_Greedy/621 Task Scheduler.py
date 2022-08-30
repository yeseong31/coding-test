# A에서 Z로 표현된 태스크가 있다.
# 각 간격마다 CPU는 한 번의 태스크만 실행할 수 있고, n번의 간격 내에는 동일한 태스크를 실행할 수 없다.
# 더 이상 태스크를 실행할 수 없는 경우 idle 상태가 된다.
# 모든 태스크를 실행하기 위한 최소 간격을 출력하라.
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        cnt = collections.Counter(tasks)
        answer = 0

        while True:
            sub_cycle = 0
            # 빈도 수가 가장 높은 (n + 1)개 원소 처리
            # 마지막 사이클만 순서 다르게 나오는 경우를 대비
            for task, c in cnt.most_common(n + 1):
                sub_cycle += 1
                answer += 1
                # 사용한 태스크의 개수를 줄임
                cnt.subtract(task)
                # 0개 이하의 태스크를 목록에서 완전히 제거(트릭)
                cnt += collections.Counter()

            if not cnt:
                break

            answer += n - sub_cycle + 1

        return answer


solution = Solution()

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(solution.leastInterval(tasks, n))
