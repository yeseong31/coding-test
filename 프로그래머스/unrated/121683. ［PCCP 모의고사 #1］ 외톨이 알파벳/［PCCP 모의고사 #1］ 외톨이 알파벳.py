from collections import defaultdict


def solution(input_string):
    answer = []
    prev = ''
    dic = defaultdict(int)
    
    for v in input_string:
        if prev == v:
            continue
        dic[v] += 1
        prev = v
    
    for k in dic.keys():
        if dic[k] >= 2:
            answer.append(k)
    
    return ''.join(sorted(answer)) if answer else 'N'