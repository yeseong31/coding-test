def solution(numbers):
    answer = []
    stack = []
    
    for i in range(len(numbers) - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        
        answer.append(stack[-1] if stack else -1)
        stack.append(numbers[i])
        
    return answer[::-1]
