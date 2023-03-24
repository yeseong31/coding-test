from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0, {begin, })])
    while q:
        cur, step, visited = q.popleft()
        if cur == target:
            return step
        lst = []
        for word in words:
            if word in visited:
                continue
            count = 0
            for c, w in zip(cur, word):
                if c == w:
                    count += 1
            if len(cur) - count == 1:
                lst.append(word)
        for l in lst:
            visited.add(l)
            q.append((l, step + 1, visited))
        
    return 0