from collections import deque


def solution(n, edge):
    answer = 0
    inf = 20000
    
    distance = [inf] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([(1, 0)])
    distance[1] = 0
    while q:
        node, dist = q.popleft()
        for x in graph[node]:
            if distance[x] == inf:
                distance[x] = dist + 1
                q.append((x, dist + 1))
    
    for i, v in enumerate(distance):
        if v == inf:
            distance[i] = -1
    
    return distance.count(max(distance))