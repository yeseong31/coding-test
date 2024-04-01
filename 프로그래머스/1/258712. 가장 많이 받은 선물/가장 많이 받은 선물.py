def solution(friends, gifts):
    n = len(friends)
    idx = {f: i for i, f in enumerate(friends)}
    graph = [[0] * n for _ in range(n)]
    
    for gift in gifts:
        a, b = gift.split(' ')
        graph[idx[a]][idx[b]] += 1
        
    scores = [0] * n
    for i in range(n):
        give_score = sum(graph[i])
        receive_score = sum(graph[x][i] for x in range(n))
        scores[i] = give_score - receive_score
    
    counts = [0] * n
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[j][i] or graph[i][j] == graph[j][i] and scores[i] > scores[j]:
                counts[i] += 1
    
    return max(counts)
