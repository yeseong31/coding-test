import collections


def solution(n, wires):
    def bfs(start):
        q = collections.deque([start])
        visited[start] = res = 1
        while q:
            for i in graph[q.popleft()]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
                    res += 1
        return res

    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:
        visited = [0] * (n + 1)
        visited[v2] = 1
        cnt = bfs(v1)
        if abs(cnt - (n - cnt)) < answer:
            answer = abs(cnt - (n - cnt))
    
    return answer