from collections import deque


def solution(n, wires):
    def bfs(start):
        q = deque([start])
        visited = [0] * (n + 1)
        visited[b] = visited[start] = 1
        
        res = 1
        while q:
            v = q.popleft()
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
                    res += 1 
        return res

    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    answer = n
    for a, b in wires:
        answer = min(answer, abs(2 * bfs(a) - n))
    return answer
