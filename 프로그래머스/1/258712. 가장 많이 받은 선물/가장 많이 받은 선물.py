from collections import defaultdict


def solution(friends, gifts):
    answer = 0
    n = len(friends)
    
    indexes = {friend: index for index, friend in enumerate(friends)}
    graph = [[0] * n for _ in range(n)]
    
    for gift in gifts:
        a, b = gift.split(' ')
        graph[indexes[a]][indexes[b]] += 1
        
    scores = [0] * n
    for index in range(n):
        give_score = sum(graph[index])
        receive_score = sum(graph[x][index] for x in range(n))
        scores[index] = give_score - receive_score
    
    receive_count = [0] * n
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[j][i] or graph[i][j] == graph[j][i] and scores[i] > scores[j]:
                receive_count[i] += 1
    
    return max(receive_count)
