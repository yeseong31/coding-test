from collections import defaultdict


def dfs(node, graph, routes):
    while graph[node]:
        dfs(graph[node].pop(), graph, routes)
    routes.append(node)
    return routes


def solution(tickets):
    graph = defaultdict(list)
    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)
    return dfs('ICN', graph, [])[::-1]
