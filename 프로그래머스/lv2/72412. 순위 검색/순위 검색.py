from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    dic = defaultdict(list)
    
    for people in info:
        people = people.split()
        score = int(people.pop())
        dic[''.join(people)].append(score)
        
        for i in range(4):
            for case in combinations(people, i):
                dic[''.join(case)].append(score)
                
    for i in dic:
        dic[i].sort()
            
    for q in query:
        q = q.split()
        target = int(q.pop())
        q = ''.join(q).replace('and', '').replace('-', '').replace(' ', '')
        
        result = len(dic[q]) - bisect_left(dic[q], target)
        answer.append(result)
            
    return answer
