# 풀이 1 - DFS로 k개 조합 생성
# 전체 수 n을 입력받아 k개의 조합을 리턴하라

def combine(n: int, k: int) -> list[list[int]]:
    result = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            result.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return result
