# 조합의 합(351p)
# 숫자 집합 condidates를 조합하여 합이 target이 되는 원소를 나열하라
# 각 원소는 중복으로 나열 가능하다
from itertools import combinations_with_replacement


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    def dfs(idx, sof, res):
        # 반복 탈출 조건: sof 값이 target과 같다면
        if sof == target:
            answer.append(res)
            return
        # 반복 탈출 조건: sof > target이라면
        elif sof > target:
            return
        # 인덱스 값 하나씩 참고해 가면서 dfs 및 백트래킹 수행
        for i in range(idx, len(candidates)):
            dfs(i, sof + candidates[i], res + [candidates[i]])

    answer = []
    # 시작 인덱스
    dfs(0, 0, [])
    return answer


# 런타임이 상대적으로 많이 길어서(376ms) 아래처럼 개선해 보았음
# 아래의 코드는 런타임이 80ms로 이전에 비해 시간이 많이 단축되었음
# (2022.02.01 수정) 위의 함수 런타임 106mx로 준수함

# def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
#     result = []
#
#     def dfs(sum_val, idx, path):
#         if sum_val < 0:
#             return
#         if sum_val == 0:
#             result.append(path)
#             return
#         for i in range(idx, len(candidates)):
#             dfs(sum_val - candidates[i], i, path + [candidates[i]])
#
#     dfs(target, 0, [])
#     return result


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))   # [[2,2,3],[7]]

# candidates = [2, 3, 5]
# target = 8
# print(combinationSum2(candidates, target))   # [[2,2,2,2],[2,3,3],[3,5]]
