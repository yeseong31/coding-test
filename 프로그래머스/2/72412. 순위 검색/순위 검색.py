from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    people = defaultdict(list)
    
    for i in info:
        person = i.split()
        score = int(person.pop())
        people[''.join(person)].append(score)
        
        for j in range(4):
            for _case in combinations(person, j):
                people[''.join(_case)].append(score)
    
    for p in people:
        people[p].sort()
        
    for q in query:
        key = q.split()
        score = int(key.pop())
        
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        
        count = len(people[key]) - bisect_left(people[key], score)
        answer.append(count)
    
    return answer