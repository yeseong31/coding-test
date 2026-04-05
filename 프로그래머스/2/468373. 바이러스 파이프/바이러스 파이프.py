from collections import deque

def solution(n, infection, edges, k):
    answer = 1

    graph = [[] for _ in range(n + 1)]
    for x, y, t in edges:
        graph[x].append((y, t))
        graph[y].append((x, t))

    def bfs(infected, type_):
        next_state = infected[:]
        queue = deque()

        for i in range(1, n + 1):
            if infected[i]:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            for to, edge_type in graph[curr]:
                if edge_type == type_ and not next_state[to]:
                    next_state[to] = True
                    queue.append(to)

        return next_state

    def dfs(step, infected):
        nonlocal answer

        count = sum(infected)
        answer = max(answer, count)

        if step == k:
            return

        for type_ in range(1, 4):
            next_state = bfs(infected, type_)
            dfs(step + 1, next_state)

    infected = [False] * (n + 1)
    infected[infection] = True

    dfs(0, infected)

    return answer