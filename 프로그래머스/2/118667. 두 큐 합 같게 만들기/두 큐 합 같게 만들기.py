from collections import deque


def solution(queue1, queue2):
    v1 = sum(queue1)
    v2 = sum(queue2)
    
    div, mod = divmod(v1 + v2, 2)
    if mod:
        return -1

    cnt = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    while q1 and q2:
        if v1 == div:
            return cnt
        
        cnt += 1
        if v1 >= div:
            v1 -= q1.popleft()
            continue
        
        pop = q2.popleft()
        q1.append(pop)
        v1 += pop

    return -1
