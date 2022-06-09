import collections


def solution(tickets):
    def dfs(v):
        while graph[v]:
            dfs(graph[v].pop())
        route.append(v)

    graph = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []
    dfs('ICN')
    return route[::-1]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
