
from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n + 1)]
    dist = [0] * (n + 1)
    q = deque([(1)])
    dist[1] = 1
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if dist[i] == 0:
                dist[i] = dist[v] + 1
                q.append(i)
    
    _max = max(dist)
    for d in dist:
        if d == _max:
            answer += 1

    return answer
