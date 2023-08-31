from collections import defaultdict


def solution(gems):
    answer = 1, len(gems)
    dic = defaultdict(int)
    length = len(set(gems))
    
    left = 0
    for right, gem in enumerate(gems):
        dic[gem] += 1
        
        while len(dic) == length:
            dic[gems[left]] -= 1
            
            if dic[gems[left]] == 0:
                if answer[1] - answer[0] > right - left:
                    answer = left + 1, right + 1
                dic.pop(gems[left])
            
            left += 1
    
    return answer
