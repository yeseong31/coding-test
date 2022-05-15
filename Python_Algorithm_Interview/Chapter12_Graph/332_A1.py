# 풀이 1 - DFS로 일정 그래프 구성
import collections


def findItinerary(tickets: list[list[str]]) -> list[str]:
    dic = collections.defaultdict(list)
    for a, b in sorted(tickets):
        dic[a].append(b)

    route = []

    def dfs(a):
        while dic[a]:
            dfs(dic[a].pop(0))  # 큐의 연산 수행
        route.append(a)

    dfs('JFK')
    return route[::-1]


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(findItinerary(tickets))
# Output: ["JFK","MUC","LHR","SFO","SJC"]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(tickets))
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]
# but it is larger in lexical order.
