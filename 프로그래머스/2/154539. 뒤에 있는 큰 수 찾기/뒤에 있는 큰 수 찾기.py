def solution(numbers):
    answer = []
    stack = []
    
    for i in range(len(numbers) - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
        
        stack.append(numbers[i])
        
    return answer[::-1]
