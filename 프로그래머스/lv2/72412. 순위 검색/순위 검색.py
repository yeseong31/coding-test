from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):    
    answer = []
    applicants = defaultdict(list)
    
    for inf in info:
        *target, score = inf.split()
        applicants[''.join(target)].append(int(score))
        for x in range(4):
            for case in combinations(target, x):
                applicants[''.join(case)].append(int(score))
    
    for i in applicants:
        applicants[i].sort()
    
    for q in query:
        *q, score = q.split()
        q = ''.join(q)
        key = q.replace('and', '').replace(' ', '').replace('-', '')
        answer.append(len(applicants[key]) - bisect_left(applicants[key], int(score)))
    return answer