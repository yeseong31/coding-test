from collections import defaultdict


def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    
    for name, kind in clothes:
        dic[kind] += 1
    for k in dic:
        answer *= dic[k] + 1
    
    return answer - 1
