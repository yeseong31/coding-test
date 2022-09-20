# 노드 수, 출발지, A 도착지, B 도착지, 요금
def solution(n, s, a, b, fares):
    INF = int(1e9)

    answer = INF
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                graph[i][j] = 0

    for v, w, fare in fares:
        graph[v][w] = fare
        graph[w][v] = fare

    for k in range(1, n + 1):
        for p in range(1, n + 1):
            for q in range(1, n + 1):
                graph[p][q] = min(graph[p][q], graph[p][k] + graph[k][q])

    # (출발 -> 분기) + (분기 -> A) + (분기 -> B) 값이 최소가 되는 구간
    for x in range(1, n + 1):
        answer = min(answer, graph[s][x] + graph[x][a] + graph[x][b])

    return answer
