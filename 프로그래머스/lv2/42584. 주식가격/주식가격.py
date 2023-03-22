def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    for i, v in enumerate(prices):
        while stack and prices[stack[-1]] > v:
            tok = stack.pop()
            answer[tok] = i - tok
        stack.append(i)
    
    for s in stack:
        answer[s] = len(prices) - 1 - s
    
    return answer