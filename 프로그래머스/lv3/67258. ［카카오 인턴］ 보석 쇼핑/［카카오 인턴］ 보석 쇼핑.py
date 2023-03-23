from collections import defaultdict


def solution(gems):
    count = len(set(gems))
    left, right = 0, len(gems) - 1
    dic = defaultdict(int)
    
    l = 0
    for r, v in enumerate(gems):
        dic[v] += 1
        if len(dic) == count:
            while l < r and dic[gems[l]] > 1:
                dic[gems[l]] -= 1
                l += 1
            if r - l < right - left:
                left, right = l, r
            
    return left + 1, right + 1
