# 조합의 합
# 숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라.
# 각 원소는 중복으로 나열 가능하다.

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def dfs(csum, idx, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        for i in range(idx, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))   # [[2,2,3],[7]]

candidates = [2, 3, 5]
target = 8
print(combinationSum(candidates, target))   # [[2,2,2,2],[2,3,3],[3,5]]
