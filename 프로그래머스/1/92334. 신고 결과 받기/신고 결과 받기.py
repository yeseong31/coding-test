from collections import defaultdict


def solution(id_list, report, k):
    sanctions = defaultdict(set)
    mail = defaultdict(int)
    
    for ids in report:
        value, key = ids.split()
        sanctions[key].add(value)
        
    for key in sanctions:
        if len(sanctions[key]) >= k:
            for v in sanctions[key]:
                mail[v] += 1
    
    return [mail[id] for id in id_list]
