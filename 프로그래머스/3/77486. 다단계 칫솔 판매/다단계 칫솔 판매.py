from collections import defaultdict


def solution(enroll, referral, seller, amount):
    graph = defaultdict(str)
    score = defaultdict(int)
    
    for e, r in zip(enroll, referral):
        graph[e] = r
        
    for s, a in zip(seller, amount):
        w = a * 100
        
        while w > 0 and s != '-':
            score[s] += w - w // 10
            w //= 10
            s = graph[s]
    
    return [score[x] for x in enroll]
