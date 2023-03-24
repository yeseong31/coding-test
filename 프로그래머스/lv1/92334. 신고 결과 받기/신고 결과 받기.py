from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    dic = defaultdict(list)
    cnt = defaultdict(int)
    
    for target in set(report):
        a, b = target.split()
        dic[a].append(b)
        cnt[b] += 1
    
    for uid in id_list:
        res = 0
        for v in dic[uid]:
            if cnt[v] >= k:
                res += 1
        answer.append(res)
    
    return answer