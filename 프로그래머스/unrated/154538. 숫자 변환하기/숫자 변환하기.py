from collections import deque


def solution(x, y, n):
    answer = 0
    q = deque([(y, 0)])
    
    while q:
        v, c = q.popleft()
        if v == x:
            return c
        if v % 3 == 0:
            q.append((v // 3, c + 1))
        if v % 2 == 0:
            q.append((v // 2, c + 1))
        if x <= v - n:
            q.append((v - n, c + 1))
            
    return -1