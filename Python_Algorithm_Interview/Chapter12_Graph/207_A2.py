# 코스 스케줄(364p)
# 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍을 표현하는 n개의 코스가 있음
# 코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.

# 풀이 2 - 가지치기를 이용한 최적화
import collections


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
