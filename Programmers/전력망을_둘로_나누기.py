# 나누었을 때 두 area의 노드 개수의 차이가 최소가 되도록!
import collections


def solution(n, wires):
    def bfs(start):
        q = collections.deque([start])
        visited[start] = 1
        res = 1
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


n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
print(solution(n, wires))
