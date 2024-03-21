from collections import defaultdict


def dfs(now, graph, result):
    while graph[now]:
        dfs(graph[now].pop(), graph, result)
    
    result.append(now)
    return result


def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
        
    for key in graph:
        graph[key].sort(reverse=True)
        
    result = []
    dfs('ICN', graph, result)
    
    return result[::-1]
