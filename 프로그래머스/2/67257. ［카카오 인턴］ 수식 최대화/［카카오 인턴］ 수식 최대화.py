import re

from collections import deque
from itertools import permutations
from math import inf


def solution(expression):
    answer = -inf
    numbers = list(re.sub('\D', '|', expression).split('|'))
    ops = list(re.sub('\d', '', expression))
    
    exp = [numbers[0]]
    for i, op in enumerate(ops):
        exp.append(op)
        exp.append(numbers[i + 1])
    
    for priority_ops in permutations('+-*', 3):
        result = calculate_result(exp, priority_ops)
        answer = max(answer, abs(result))
    
    return answer


def calculate_result(exp, priority_ops):
    exp_q = deque(exp)
    mid_q = deque()
    
    for priority_op in priority_ops:
        while exp_q:
            x = exp_q.popleft()
            
            if x.isdigit() or x != priority_op:
                mid_q.append(x)
                continue
            
            n1 = mid_q.pop()
            n2 = exp_q.popleft()
            mid_q.append(calculate(n1, n2, x))
        
        exp_q = mid_q.copy()
        mid_q = deque()
        
    result = exp_q.popleft()
    return int(result)
        

def calculate(number1, number2, op):
    number1, number2 = int(number1), int(number2)
    if op == '+':
        return str(number1 + number2)
    elif op == '-':
        return str(number1 - number2)
    else:
        return str(number1 * number2)
