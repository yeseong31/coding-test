def count_forward(u, graph, visited):
    result = 1
    
    for v in range(len(graph[u])):
        if not graph[u][v] or visited[v]:
            continue
        
        visited[v] = True
        result += count_forward(v, graph, visited)
    
    return result


def count_backward(u, graph, visited):
    result = 1
    
    for v in range(len(graph[u])):
        if not graph[v][u] or visited[v]:
            continue
        
        visited[v] = True
        result += count_backward(v, graph, visited)
    
    return result


def solution(n, results):
    answer = 0
    graph = [[False] * n for _ in range(n)]
    
    for a, b in results:
        graph[a - 1][b - 1] = True
    
    for u in range(n):
        wins = count_forward(u, graph, [False] * n) - 1
        loses = count_backward(u, graph, [False] * n) - 1
        
        if wins + loses == n - 1:
            answer += 1
    
    return answer
