import re
from itertools import permutations


def toPostFix(tokens, priority):
    stack = []
    result = []
    
    for token in tokens:
        if token.isdigit():
            result.append(token)
            continue
        
        if not stack:
            stack.append(token)
            continue
        
        while stack and priority[token] <= priority[stack[-1]]:
            result.append(stack.pop())
        
        stack.append(token)
        
    while stack:
        result.append(stack.pop())
    
    return result


def calculate(tokens):
    stack = []
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue
            
        num2, num1 = stack.pop(), stack.pop()
        if token == '+':
            stack.append(num1 + num2)
        elif token == '-':
            stack.append(num1 - num2)
        else:
            stack.append(num1 * num2)
    
    return stack.pop()


def solution(expression):
    answer = 0
    tokens = re.split(r'([-+*])|\s+', expression)
    operators = ('+', '-', '*')
    
    for _case in map(list, permutations(operators)):
        priority = {o: p for p, o in enumerate(list(_case))}
        postfix = toPostFix(tokens, priority)
        answer = max(answer, abs(calculate(postfix)))
    
    return answer
