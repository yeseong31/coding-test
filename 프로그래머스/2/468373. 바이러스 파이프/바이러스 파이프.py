from collections import deque

def solution(n, infection, edges, k):
    graph = [[] for _ in range(n + 1)]
    for a, b, t in edges:
        graph[a].append((b, t))
        graph[b].append((a, t))

    max_infected = [1]
    infected = [False] * (n + 1)
    infected[infection] = True

    def bfs(infected, edge_type):
        next_state = infected[:]
        queue = deque(i for i in range(1, n + 1) if infected[i])
        while queue:
            curr = queue.popleft()
            for to, t in graph[curr]:
                if t == edge_type and not next_state[to]:
                    next_state[to] = True
                    queue.append(to)
        return next_state

    def dfs(step, infected):
        max_infected[0] = max(max_infected[0], sum(infected))
        if step == k:
            return
        for edge_type in range(1, 4):
            dfs(step + 1, bfs(infected, edge_type))

    dfs(0, infected)
    return max_infected[0]