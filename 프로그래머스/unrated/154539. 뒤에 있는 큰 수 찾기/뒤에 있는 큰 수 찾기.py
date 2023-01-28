from collections import deque


def solution(numbers):
    answer = deque()
    stack = []
    
    for i in range(len(numbers) - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        if not stack:
            answer.appendleft(-1)
        else:
            answer.appendleft(stack[-1])
        stack.append(numbers[i])
        
    return list(answer)