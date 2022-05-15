# 부분 집합(355p)
# 모든 부분 집합을 리턴하라

def subsets(nums: list[int]) -> list[list[int]]:
    def dfs(idx, res):
        answer.append(res)
        for i in range(idx, len(nums)):
            dfs(i + 1, res + [nums[i]])

    answer = []
    dfs(0, [])
    return answer


nums = [1, 2, 3]
print(subsets(nums))
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Input: nums = [0]
# Output: [[],[0]]
