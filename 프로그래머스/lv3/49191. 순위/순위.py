def solution(n, results):
    answer = [0] * n
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for a, b in results:
        graph[a][b] = 1
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == graph[k][j] == 1:
                    graph[i][j] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            answer[i - 1] += graph[i][j]
            answer[j - 1] += graph[i][j]

    return answer.count(n - 1)