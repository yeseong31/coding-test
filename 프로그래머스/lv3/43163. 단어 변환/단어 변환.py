from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    while q:
        cur, i = q.popleft()
        if cur == target:
            return i
        next_words = [word for word in words if len(cur) - 1 == sum(c == w for c, w in zip(cur, word))]
        if not next_words:
            return 0
        for nw in next_words:
            q.append((nw, i + 1))
        
    return 0