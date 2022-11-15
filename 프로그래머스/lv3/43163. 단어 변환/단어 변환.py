from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    
    length = len(begin)
    q = deque([(begin, 0)])
    visited = set()
    
    while q:
        cur_word, cnt = q.popleft()
        if cur_word == target:
            return cnt
        for target_word in words:
            if target_word in visited:
                continue
            check = 0
            for a, b in zip(cur_word, target_word):
                if a == b:
                    check += 1
            if length - check == 1:
                q.append((target_word, cnt + 1))
    
    return answer