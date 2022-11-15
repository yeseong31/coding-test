def solution(n, computers):
    def dfs(x):
        visited[x] = True
        for k in range(n):
            if not visited[k] and computers[x][k] == 1:
                dfs(k)

    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
