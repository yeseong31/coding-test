def is_valid_case(queue, answer, current_case):
    for q, ans in zip(queue, answer):
        if sum(c in q for c in current_case) != ans:
            return False
        
    return True


def solution(n, q, ans):
    def dfs(x, current_case, result):
        if len(current_case) == 5:
            if is_valid_case(q, ans, current_case):
                result.append(current_case)
            return
        
        if x <= n:
            dfs(x + 1, current_case, result)
            dfs(x + 1, current_case + [x], result)
    
    result = []
    dfs(1, [], result)
    return len(result)