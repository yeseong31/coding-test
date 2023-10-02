import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


def solution():
    def dfs(x, y):
        for k, d in graph[x]:
            if visited[k] == -1:
                visited[k] = d + y
                dfs(k, d + y)
        
    v = int(input())
    graph = [[] for _ in range(v + 1)]
    
    for _ in range(v):
        line = list(map(int, input().split()))
        for j in range(1, len(line) - 2, 2):
            graph[line[0]].append((line[j], line[j + 1]))
            
    visited = [-1] * (v + 1)
    visited[1] = 0
    dfs(1, 0)
    
    start = visited.index(max(visited))
    
    visited = [-1] * (v + 1)
    visited[start] = 0
    dfs(start, 0)
    
    return max(visited)


print(solution())
