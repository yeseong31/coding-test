def solution(n, s, a, b, fares):
    inf = int(1e9)
    graph = [[inf] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
                
    for v, w, c in fares:
        graph[v][w] = graph[w][v] = c
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    return min(graph[s][i] + graph[i][a] + graph[i][b] for i in range(1, n + 1))