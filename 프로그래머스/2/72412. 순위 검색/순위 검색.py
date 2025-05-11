from bisect import bisect_left
from collections import defaultdict


def solution(info, query):
    answer = []
    scores = defaultdict(list)
    
    for i in info:
        *cond, score = i.split()
        
        cases = []
        get_cases(cond, 0, [], cases)
        
        for key in cases:
            scores[key].append(int(score))
    
    for key in scores:
        scores[key].sort()
    
    for q in query:
        *cond, score = q.split()
        score = int(score)
        
        key = ''.join(cond).replace('and', '')
        values = scores[key]
        
        index = bisect_left(values, score)
        answer.append(len(values) - index)
    
    return answer


def get_cases(cond, seq, current, cases):
    if seq == len(cond):
        if current:
            cases.append(''.join(current))
        return
    
    get_cases(cond, seq + 1, current + [cond[seq]], cases)
    get_cases(cond, seq + 1, current + ['-'], cases)
    