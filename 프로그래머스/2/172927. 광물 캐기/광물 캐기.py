from collections import deque


def solution(picks, minerals):
    answer = 10000
    choice = {'diamond': 0, 'iron': 1, 'stone': 2}
    scores = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    q = deque([(0, -1, 0, *picks)])
    
    while q:
        i, c, total, *pick = q.popleft()
        
        if total > 0:
            pick[c] -= 1
        
        if i >= len(minerals) or sum(pick) == 0:
            answer = min(answer, total)
            continue
        
        for a in range(3):
            if pick[a] != 0:
                res = sum(scores[a][choice[minerals[b]]] for b in range(i, i + 5) if b < len(minerals))
                q.append((i + 5, a, total + res, *pick))

    return answer
