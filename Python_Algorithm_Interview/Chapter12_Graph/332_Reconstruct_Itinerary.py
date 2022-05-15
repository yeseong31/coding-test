# 일정 재구성(357p)
# [from, to]로 구성된 항공권 목록을 이용하여 JFK에서 출발하는 여행 일정을 구성하라.
# 여러 일정이 있는 경우 사전 어휘 순으로 방문한다.
import collections


def findItinerary(tickets: list[list[str]]) -> list[str]:
    board = collections.defaultdict(list)
    for ticket_from, ticket_to in sorted(tickets, reverse=True):
        board[ticket_from].append(ticket_to)

    def dfs(place):
        while board[place]:
            dfs(board[place].pop())
        answer.append(place)

    answer = []
    dfs('JFK')
    return answer[::-1]


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(findItinerary(tickets))
# Output: ["JFK","MUC","LHR","SFO","SJC"]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(tickets))
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]
# but it is larger in lexical order.
