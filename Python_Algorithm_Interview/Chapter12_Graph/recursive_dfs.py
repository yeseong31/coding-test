# 재귀 구조로 DFS 구현

def dfs(v, graph, discovered=[]):
    discovered.append(v)
    for i in graph[v]:
        if i not in discovered:
            discovered = dfs(i, graph, discovered)
    return discovered
