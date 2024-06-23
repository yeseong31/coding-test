from collections import defaultdict


def solution(id_list, report, k):
    sanctions = defaultdict(set)
    mail = defaultdict(int)
    
    for ids in report:
        report_id, reported_id = ids.split()
        sanctions[reported_id].add(report_id)
        
    for key in sanctions:
        if len(sanctions[key]) < k:
            continue
        for v in sanctions[key]:
            mail[v] += 1
    
    return [mail[id] for id in id_list]
