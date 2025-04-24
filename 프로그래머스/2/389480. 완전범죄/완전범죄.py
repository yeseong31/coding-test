def solution(info, n, m):
    answer = [n]
    visited = set()

    def dfs(i, a, b):
        if (i, a, b) in visited:
            return
        
        visited.add((i, a, b))
        
        if a >= n or b >= m or a >= answer[0]:
            return
        if i == len(info):
            answer[0] = min(answer[0], a)
            return

        dfs(i + 1, a + info[i][0], b)
        dfs(i + 1, a, b + info[i][1])

    dfs(0, 0, 0)
    return answer[0] if answer[0] != n else -1
