# 스택을 이용한 반복 구조로 구현

def dfs(start, graph):
    discovered = []
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for i in graph[v]:
                stack.append(i)
    return discovered

