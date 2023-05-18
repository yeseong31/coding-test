def solution(s):
    stack = []
    for c in s:
        if stack and c == ')':
            stack.pop()
        else:
            stack.append(c)
    
    return not stack