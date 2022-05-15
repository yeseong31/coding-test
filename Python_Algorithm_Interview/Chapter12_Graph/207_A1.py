# 풀이 1 - DFS로 순환 구조 판별
import collections


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    dic = collections.defaultdict(list)
    for a, b in prerequisites:
        dic[a].append(b)

    # 사이클 판별
    def dfs(x):
        if x in visited:
            return False
        visited.add(x)
        for y in dic[x]:
            if not dfs(y):
                return False
        visited.remove(x)
        return True

    # 방문 처리
    visited = set()
    for i in list(dic):
        if not dfs(i):
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
