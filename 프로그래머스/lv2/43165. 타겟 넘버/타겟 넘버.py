def solution(numbers, target):
    def dfs(idx, val):
        if idx == len(numbers):
            return 1 if val == target else 0
        return dfs(idx + 1, val + numbers[idx]) + dfs(idx + 1, val - numbers[idx])
    
    return dfs(0, 0)