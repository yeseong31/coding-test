def solution(number, k):
    stack = []
    
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    
    while k > 0:
        stack.pop()
        k -= 1
    
    return ''.join(stack)