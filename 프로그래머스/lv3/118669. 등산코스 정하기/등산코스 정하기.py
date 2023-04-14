from heapq import heapify, heappush, heappop


def solution(n, paths, gates, summits):
    answer = [0, 10000001]
    graph = [[] for _ in range(n + 1)]
    for a, b, c in paths:
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    def dijkstra(start):
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
    
    summits_set = set(summits)
    gates_set = set(gates)
    intensity = [10000001] * (n + 1)
    for gate in gates:
        dijkstra(gate)
    
    for summit in summits_set:
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
        elif intensity[summit] == answer[1]:
            answer[0] = min(summit, answer[0])
    
    return answer
