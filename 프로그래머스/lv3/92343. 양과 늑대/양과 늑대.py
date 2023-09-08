def solution(info, edges):
    def dfs(sheep, wolf):
        if sheep <= wolf:
            return
        
        answer.append(sheep)
        for parent, child in edges:
            check = (info[child] == 1)
            if visited[parent] and not visited[child]:
                visited[child] = True
                dfs(sheep + (not check), wolf + check)
                visited[child] = False
    
    answer = []
    visited = [False] * len(info)
    visited[0] = True
    
    dfs(1, 0)
    
    return max(answer)