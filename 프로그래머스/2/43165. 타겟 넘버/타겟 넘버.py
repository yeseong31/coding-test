def dfs(seq, target, numbers, result):
    if seq == len(numbers):
        result.append(target == 0)
        return
    
    dfs(seq + 1, target + numbers[seq], numbers, result)
    dfs(seq + 1, target - numbers[seq], numbers, result)
    

def solution(numbers, target):
    answer = []
    dfs(0, target, numbers, answer)
    return sum(answer)
