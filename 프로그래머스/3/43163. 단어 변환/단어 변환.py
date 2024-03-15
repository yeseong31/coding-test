from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    
    while q:
        current_word, count = q.popleft()
        
        if current_word == target:
            return count
        
        target_words = [word for word in words if len(current_word) - 1 == sum(c == w for c, w in zip(current_word, word))]
        
        for word in target_words:
            q.append((word, count + 1))
        
    return 0
