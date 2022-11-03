# Reconstruct Itinerary
import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = collections.defaultdict(list)
        for a, b in sorted(tickets):    # 사전 어휘 순 저장
            dic[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while dic[stack[-1]]:
                stack.append(dic[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]
