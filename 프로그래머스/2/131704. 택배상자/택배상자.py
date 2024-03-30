def solution(order):
    answer = []
    stack = []
    
    i, j = 1, 0
    
    while i <= len(order):
        while stack and stack[-1] == order[j]:
            answer.append(stack.pop())
            j += 1
            
        if i != order[j]:
            stack.append(i)
        else:
            answer.append(i)
            j += 1
            
        i += 1
        
    while stack and stack[-1] == order[j]:
        answer.append(stack.pop())
        j += 1
    
    return len(answer)
