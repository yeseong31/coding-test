from collections import defaultdict


def solution(genres, plays):
    answer = []
    dic = defaultdict(int)
    q = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        dic[g] += p
        q[g].append((i, p))

    for k in sorted(dic.items(), key=lambda x: x[1], reverse=True):
        for i, _ in sorted(q[k[0]], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
