# 풀이 2 - 스택 연산으로 큐 연산 최적화 시도
import collections


def findItinerary(tickets: list[list[str]]) -> list[str]:
    dic = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        dic[a].append(b)

    route = []

    def dfs(a):
        while dic[a]:
            dfs(dic[a].pop())
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
