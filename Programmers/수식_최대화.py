import copy
from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    exp = deque()

    num = ''
    for e in expression:
        if e.isdigit():
            num += e
        else:
            exp.append(num)
            exp.append(e)
            num = ''
    exp.append(num)

    for permutation in list(permutations(['+', '-', '*'], 3)):
        q = copy.deepcopy(exp)
        for p in permutation:
            stack = deque()
            while q:
                v = q.popleft()
                if v == p:
                    stack.append(str(eval(str(stack.pop()) + p + str(q.popleft()))))
                else:
                    stack.append(v)
            q = stack
        answer = max(answer, abs(int(q[0])))

    return answer