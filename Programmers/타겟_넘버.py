def solution(numbers, target):
    answer = 0

    def dfs(numbers, target, idx):
        result = 0
        # 탈출 조건
        if idx == len(numbers):
            if sum(numbers) == target:
                return 1
            else:
                return 0
        # 끝에 도달한 게 아니라면
        else:
            result += dfs(numbers, target, idx + 1)
            numbers[idx] *= -1
            result += dfs(numbers, target, idx + 1)
            return result

    answer = dfs(numbers, target, 0)
    return answer