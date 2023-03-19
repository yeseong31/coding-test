import re
from itertools import permutations


def calculate(exp):
    stack = []
    for tok in exp:
        if tok.isdigit():
            stack.append(int(tok))
            continue
        m, n = stack.pop(), stack.pop()
        if tok == '+':
            stack.append(n + m)
        elif tok == '-':
            stack.append(n - m)
        else:
            stack.append(n * m)
    return abs(stack.pop())


def to_postfix(tokens, priority):
    ops, result = [], []
    for token in tokens:
        if token.isdigit():
            result.append(token)
            continue
        if not ops:
            ops.append(token)
            continue
        while ops:
            if priority[token] > priority[ops[-1]]:
                break
            result.append(ops.pop())
        ops.append(token)
        
    while ops:
        result.append(ops.pop())
    return result


def solution(expression):
    answer = 0
    tokens = re.split(r'([-+*])|\s+', expression)
    
    for x in permutations(('+', '-', '*')):
        priority = {v: i for i, v in enumerate(list(x))}
        exp = to_postfix(tokens, priority)
        answer = max(answer, calculate(exp))
    
    return answer
