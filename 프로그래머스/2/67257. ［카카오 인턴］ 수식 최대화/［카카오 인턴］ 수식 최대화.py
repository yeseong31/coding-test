from copy import deepcopy


def split(expression):
    result = []
    prev = ''

    for c in expression:
        if c.isdigit():
            prev += c
            continue
        
        result.append(int(prev))
        result.append(c)
        prev = ''

    result.append(prev)
    return result


def calculate(tokens, operator):
    stack = []

    for op in operator:
        for token in tokens:
            if stack and stack[-1] == op:
                target_op = stack.pop()
                left_number = stack.pop()
                stack.append(eval(f'{left_number}{target_op}{token}'))
            else:
                stack.append(token)

        tokens = deepcopy(stack)

    return abs(int(stack.pop()))


def solution(expression):
    operators = (('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+'))
    tokens = split(expression)
    return max(calculate(tokens, operator) for operator in operators)
