from collections import deque


def solution(n, edge):
    def bfs(start: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for a, b in edge:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n + 1)
        distance = [20001] * (n + 1)

        q = deque()
        q.append((start, 0))
        visited[start] = True
        distance[start] = 0

        while q:
            v, d = q.popleft()
            for x in graph[v]:
                if not visited[x]:
                    visited[x] = True
                    distance[x] = min(distance[x], d + 1)
                    q.append((x, distance[x]))

        for i, v in enumerate(distance):
            if v == 20001:
                distance[i] = -1

        return distance.count(max(distance))

    return bfs(1)


n, edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
