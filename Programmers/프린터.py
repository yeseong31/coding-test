from collections import deque

def solution(priorities, location):
    q = deque((i, v) for i, v in enumerate(priorities))
    cnt = 1
    while q:
        idx, val = q.popleft()
        if any(val < x for _, x in q):
            q.append((idx, val))
        else:
            if idx == location:
                return cnt
            cnt += 1