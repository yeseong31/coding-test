from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque()
    for p, s in zip(progresses, speeds):
        q.append((p, math.ceil((100 - p) / s)))
    count = 0   # 지난 일 수
    while q:
        n = 1       # 배포 기능 수
        count = max(count, q.popleft()[1])
        while q:
            a, b = q.popleft()
            if count < b:
                q.appendleft((a, b))
                answer.append(n)
                break
            n += 1
    return answer