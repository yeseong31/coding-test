from math import ceil
from collections import deque


def solution(progresses, speeds):
    answer = []
    q = deque()
    cnt = 0
    
    for p, s in zip(progresses, speeds):
        day = ceil((100 - p) / s)
        
        while q and q[0] < day:
            q.popleft()
            cnt += 1
        q.append(day)
        
        if cnt > 0:
            answer.append(cnt)
            cnt = 0
    
    answer.append(len(q))
    return answer