def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for t, v in enumerate(prices):
        while stack and stack[-1][1] > v:
            i, _ = stack.pop()
            answer[i] = t - i
        
        stack.append((t, v))
        
    while stack:
        i, _ = stack.pop()
        answer[i] = len(answer) - 1 - i
    
    return answer