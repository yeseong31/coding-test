# 큐를 이용한 반복 구조로 bfs 구현
from collections import deque


def bfs(start, graph):
    discovered = [start]
    q = deque([start])
    while q:
        v = q.pop()
        for i in graph[v]:
            if i not in discovered:
                discovered.append(i)
                q.append(i)
    return discovered
