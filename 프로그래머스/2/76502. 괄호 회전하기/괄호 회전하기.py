from collections import deque


def solution(s):
    answer = 0
    q = deque(s)
    
    pairs = {
        ']': '[',
        ')': '(',
        '}': '{',
    }
    
    for _ in range(len(q)):
        answer += is_valid(q, pairs)
        q.append(q.popleft())
    
    return answer


def is_valid(q, pairs):
    stack = []
    
    for _, v in enumerate(q):
        if v not in pairs:
            stack.append(v)
        elif stack and stack[-1] == pairs[v]:
            stack.pop()
        else:
            return False

    return not stack
