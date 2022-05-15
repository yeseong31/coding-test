# 코스 스케줄(364p)
# 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍을 표현하는 n개의 코스가 있음
# 코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.
# ... 사이클 판별 문제라고 봐도 될 듯
import collections


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    def dfs(node):
        # 순환 구조라면 False
        if node in traced:
            return False
        # 이미 방문했던 곳이라면 True
        if node in visited:
            return True

        # set에 추가
        traced.add(node)
        for y in graph[node]:
            if not dfs(y):
                return False
        # 확인이 끝났으면 해당 node는 set에서 제거
        traced.remove(node)
        visited.add(node)

        return True

    # 순환 구조 판별을 위해 변수 지정(중복 X)
    traced = set()
    visited = set()

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True

numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))
# Output: true

numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(canFinish(numCourses, prerequisites))
# Output: false
