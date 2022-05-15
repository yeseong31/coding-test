# 실전 문제 - 커리큘럼(303p)

from collections import deque

# 강의의 수
n = int(input())
# 진입차수
indegree = [0] * (n + 1)
# 그래프
graph = [[] for _ in range(n + 1)]
# 강의시간
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in range(1, len(data) - 1):
        graph[data[j]].append(i)
        indegree[i] += 1


def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for k in graph[now]:
            indegree[k] -= 1
            if indegree[k] == 0:
                q.append(k)
                time[k] += time[now]


topology_sort()
for i in range(1, n + 1):
    print(time[i])
