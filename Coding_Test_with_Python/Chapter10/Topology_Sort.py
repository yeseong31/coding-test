# 위상 정렬
# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
# 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
# '선수과목을 고려한 학습 순서 설정' 문제에 사용할 수 있음

# 알고리즘
# 1) 진입차수가 0인 노드를 큐에 넣음
# 2) 큐가 빌 때까지 다음의 과정을 반복함
#     (i)  큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#     (ii) 새롭게 진입차수가 0이 된 노드를 큐에 넣음

# 이때 모든 원소를 방문하지 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있음
# 또한 위상 정렬의 답안은 여러 가지가 될 수 있다는 점이 특징

from collections import deque

# 노드 개수, 간선 개수
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담는 그래프
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1    # 진입차수 1 증가


# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수를 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')


topology_sort()

# 입력 예시
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# 출력 예시
# 1 2 5 3 6 4 7

# 시간 복잡도: O(V + E)
