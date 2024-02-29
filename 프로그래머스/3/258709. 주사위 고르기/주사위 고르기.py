from itertools import combinations, product
from bisect import bisect_left


def get_scores(_case):
    result = []
    
    for prod in product(range(6), repeat=len(_case)):
        result.append(sum(p[i] for i, p in zip(prod, _case)))
    
    return sorted(result)


def solution(dice):
    answer = []
    _max = 0
    
    for _case in combinations(range(len(dice)), len(dice) // 2):
        a_case = set(_case)
        b_case = set(range(len(dice))) - a_case
        
        a_scores = get_scores([dice[i] for i in a_case])
        b_scores = get_scores([dice[i] for i in b_case])
        
        a_wins = sum(bisect_left(b_scores, a_score) for a_score in a_scores)
        
        if _max < a_wins:
            _max = a_wins
            answer = list(map(lambda x: x + 1, _case))
    
    return answer
