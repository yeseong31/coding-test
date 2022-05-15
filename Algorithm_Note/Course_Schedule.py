# 코스 스케줄(364p)
# 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍을 표현하는 n개의 코스가 있음
# 코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.

# -------------------------------------------------------------------------------
# 풀이 1 - DFS로 순환 구조 판별
import collections


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    dic = collections.defaultdict(list)
    for a, b in prerequisites:
        dic[a].append(b)

    # 사이클 판별    (서로소 집합을 이용한 사이클 판별은 'Disjoint_Sets_with_Path_Compress.py' 참고)
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

# -------------------------------------------------------------------------------

# 풀이 2 - 가지치기를 이용한 최적화


# 코스 개수 numCourses, 선후수 관계를 표현하는 리스트 prerequisites
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    dic = collections.defaultdict(list)
    for a, b in prerequisites:
        dic[a].append(b)

    traced = set()      # 순환 구조 판별
    visited = set()     # 최종적으로 방문한 노드 기록을 남김

    def dfs(x):
        # 순환 구조이면 False
        if x in traced:
            return False
        # 이미 방문했던 노드이면 True
        if x in visited:
            return True

        traced.add(x)
        for y in dic[x]:
            if not dfs(y):
                return False

        # 탐색 종료 후 순환 노드 삭제
        traced.remove(x)
        # 탐색 종료 후 방문 노드 추가
        visited.add(x)
        return True

    for d in list(dic):
        if not dfs(d):
            return False

    return True

# DFS는 순환이 발견될 때까지 모든 자식 노드를 탐색하는 구조로 되어 있음
# 이러한 이유로 DFS는 불필요하게 동일한 그래프를 여러 번 탐색하는 문제가 있음
# 따라서 한 번 방문했던 그래프는 두 번 다시 방문하지 않도록 무조건 True로 리턴하는 구조로 개선해야 함

# ---------------------------------------------------------------------------------------
# [defaultdict 순회 문제]
# defaultdict를 사용하여 키가 없는 딕셔너리에 대해서 빈 값을 조회할 경우 null이 없도록 했는데,
# 이 때문에 for문 등의 반복문에서 오류가 발생할 수 있음
# 이에 대한 해결책으로는 딕셔너리 타입을 list()로 감싸서 새로운 복사본을 만드는 방법이 있음
