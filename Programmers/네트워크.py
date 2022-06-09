# 컴퓨터의 개수, 연결정보
def solution(n, computers):
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if computers[v][i] and not visited[i]:
                dfs(i)

    count = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
