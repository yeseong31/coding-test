def solution(s):
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif stack and stack[-1] == '(':
            stack.pop();
        else:
            return False
    
    return not stack
