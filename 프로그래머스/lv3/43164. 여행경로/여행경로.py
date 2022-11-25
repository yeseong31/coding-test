from collections import defaultdict


def solution(tickets):
    def dfs(v):
        while graph[v]:
            dfs(graph[v].pop())
        answer.append(v)
    
    graph = defaultdict(list)
    for s, e in sorted(tickets, reverse=True):
        graph[s].append(e)
    
    answer = []
    dfs('ICN')
    return answer[::-1]