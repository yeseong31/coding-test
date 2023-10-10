from collections import defaultdict


def solution(scores):
    answer = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    max_p = 0
    rank = 1
    
    for w, p in scores:
        if answer[0] < w and answer[1] < p:
            return -1
        if max_p <= p:
            max_p = p
            if sum(answer) < w + p:
                rank += 1
            
    return rank
