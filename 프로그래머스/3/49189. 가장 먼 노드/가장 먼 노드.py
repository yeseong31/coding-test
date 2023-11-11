from collections import deque


def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [0] * (n + 1)
    distance[1] = 1
    
    q = deque([1])
    
    while q:
        node = q.popleft()
        
        for v in graph[node]:
            if distance[v] != 0:
                continue
                
            distance[v] = distance[node] + 1
            q.append(v)
    
    return distance.count(max(distance))