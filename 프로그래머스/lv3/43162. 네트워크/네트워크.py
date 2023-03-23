def dfs(n, idx, computers, visited):
    visited[idx] = True
    for i in range(n):
        if not visited[i] and computers[idx][i] == 1:
            dfs(n, i, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(n, i, computers, visited)
            answer += 1
    return answer