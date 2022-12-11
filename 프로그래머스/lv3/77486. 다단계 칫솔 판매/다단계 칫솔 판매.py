from collections import defaultdict


def solution(enroll, referral, seller, amount):
    graph = defaultdict(str)
    score = defaultdict(int)
    for enr, ref in zip(enroll, referral):
        graph[enr] = ref
    for slr, amt in zip(seller, amount):
        won = amt * 100
        while won > 0 and slr != '-':
            score[slr] += won - won // 10
            won //= 10
            slr = graph[slr]
    return [score[x] for x in enroll]