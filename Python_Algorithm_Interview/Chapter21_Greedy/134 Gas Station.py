# 원형으로 경로가 연결된 주유소 목록이 있다.
# 각 주유소는 gas[i]만큼의 기름을 갖고 있으며, 다음 주유소로 이동하는데 cost[i]가 필요하다.
# 기름이 부족하면 이동할 수 없다고 할 때 모든 주유소를 방문할 수 있는 출발점의 인덱스를 출력하라.
# 출발점이 존재하지 않을 경우 -1을 리턴하며, 출발점은 유일하다.
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # 출발점, 연료
        start = fuel = 0
        for i in range(len(gas)):
            # 출발할 수 없는 지점은 제외
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start


solution = Solution()

# 0번 주유소에서 1만큼 충전 가능, 1번으로 이동할 때 3만큼 소비
gas = [1, 2, 3, 4, 5, 5, 70]
cost = [2, 3, 4, 3, 9, 6, 2]
print(solution.canCompleteCircuit(gas, cost))
