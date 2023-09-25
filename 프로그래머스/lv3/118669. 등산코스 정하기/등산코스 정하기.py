from heapq import heapify, heappush, heappop


def dijkstra(start, graph, summits_set, gates_set, intensity):
    q = []
    intensity[start] = 0
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)
        if now in summits_set or dist > intensity[now]:
            continue

        for c, v in graph[now]:
            if v in gates_set:
                continue

            cost = max(intensity[now], c)
            if intensity[v] <= cost:
                continue

            intensity[v] = cost
            heappush(q, (cost, v))


def solution(n, paths, gates, summits):
    _min, _max = 0, int(1e8)
    graph = [[] for _ in range(n + 1)]
    
    for a, b, c in paths:
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    summits_set = set(summits)
    gates_set = set(gates)
    
    intensity = [int(1e8)] * (n + 1)
    for gate in gates:
        dijkstra(gate, graph, summits_set, gates_set, intensity)
    
    for s in summits_set:
        if intensity[s] < _max:
            _min, _max = s, intensity[s]
        elif intensity[s] == _max:
            _min = min(s, _min)
    
    return _min, _max
