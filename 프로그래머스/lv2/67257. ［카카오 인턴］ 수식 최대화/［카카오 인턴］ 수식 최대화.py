import re
from itertools import permutations


def to_postfix(token_list, ops):
    result, stack = [], []
    priorities = {v: i for i, v in enumerate(ops)}
    
    for t in token_list:
        if t.isdigit():
            result.append(t)
            continue
        # 연산자 스택이 비어 있다면 스택에 추가
        if not stack:
            stack.append(t)
            continue
        # 연산자 스택에 쌓인 연산자와 현재 연산자의 우선순위 비교
        while stack:
            if priorities[t] < priorities[stack[-1]]:
                break
            result.append(stack.pop())
        # 현재 연산자를 스택에 추가
        stack.append(t)
    # 연산자 스택에 남아 있는 연산자들을 result에 추가
    while stack:
        result.append(stack.pop())
    return result


def calcul_postfix(exp):
    result, stack = 0, []
    
    for x in exp:
        if x.isdigit():
            stack.append(int(x))
            continue
        # 연산자라면 연산 수행 후 스택에 추가
        num2, num1 = stack.pop(), stack.pop()
        if x == '+':
            stack.append(num1 + num2)
        elif x == '-':
            stack.append(num1 - num2)
        elif x == '*':
            stack.append(num1 * num2)
    
    return abs(stack.pop())


def solution(expression):
    answer = 0
    tokens = re.split(r'([-+*])|\s+', expression)
    
    for p in permutations(('+', '-', '*'), 3):
        # 후위 연산자로 변환
        post_exp = to_postfix(tokens, p)
        # 수식 계산 후 최댓값 저장
        answer = max(answer, calcul_postfix(post_exp))
    
    return answer
