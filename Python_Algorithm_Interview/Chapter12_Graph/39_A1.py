# 풀이 1 - DFS로 중복 조합 그래프 탐색

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def dfs(csum, idx, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        # 자신부터 하위 원소까지의 나열 재귀 호출
        for i in range(idx, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])    # 두 번째 인자를 0으로 주면 '순열'로 풀이하게 됨

    dfs(target, 0, [])
    return result


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))   # [[2,2,3],[7]]

candidates = [2, 3, 5]
target = 8
print(combinationSum(candidates, target))   # [[2,2,2,2],[2,3,3],[3,5]]

# 테스트 케이스 입력값에 0이 포함되어 있다면 종료 조건을 만족할 수 없기 때문에 무한히 깊이 탐색을 시도하게 되는 문제가 있음
