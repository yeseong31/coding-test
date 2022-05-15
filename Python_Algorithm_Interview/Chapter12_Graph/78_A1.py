# 풀이 1 - 트리의 모든 DFS 결과

def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def dfs(idx, path):
        # 매번 결과 추가
        result.append(path)

        # 경로를 만들면서 dfs
        for i in range(idx, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Input: nums = [0]
# Output: [[],[0]]
