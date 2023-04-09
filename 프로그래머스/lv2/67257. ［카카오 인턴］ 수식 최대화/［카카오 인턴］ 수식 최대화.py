import re
from itertools import permutations


def calc(target):
    stack = []
    for t in target:
        if t.isdigit():
            stack.append(int(t))
            continue
        n2, n1 = stack.pop(), stack.pop()
        if t == '+':
            stack.append(n1 + n2)
        elif t == '-':
            stack.append(n1 - n2)
        else:
            stack.append(n1 * n2)
    return stack.pop()

def to_postfix(tokens, priority):
    stack, result = [], []
    
    for token in tokens:
        if token.isdigit():
            result.append(token)
            continue
        if not stack:
            stack.append(token)
            continue
        # 우선순위가 낮다면 더 이상 낮아지지 않을 때까지 스택 비우기
        while stack:
            if priority[token] < priority[stack[-1]]:
                break
            result.append(stack.pop())
        stack.append(token)

    while stack:
        result.append(stack.pop())
    return calc(result)


def solution(expression):
    answer = 0
    tokens = re.split(r'([-+*])|\s+', expression)
    for perm in permutations(['+', '-', '*'], 3):
        priority = {v: i for i, v in enumerate(perm)}
        answer = max(answer, abs(to_postfix(tokens, priority)))
    return answer
