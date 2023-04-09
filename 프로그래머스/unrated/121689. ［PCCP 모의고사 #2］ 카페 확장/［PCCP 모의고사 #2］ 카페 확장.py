from collections import deque


def solution(menu, order, k):
    answer = 0
    q = deque()
    working = -1
    i = 0
    
    for t in range(k * (len(order) - 1) + 1):
        if k * i == t:
            q.append(menu[order[i]])
            i += 1
        if working == t:
            q.popleft()
            working = -1
        if q and working == -1:
            working = t + q[0]
        answer = max(answer, len(q))
    
    return answer