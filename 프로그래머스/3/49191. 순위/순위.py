from collections import defaultdict


def solution(n, results):
    answer = [0] * n
    
    wins = defaultdict(set)
    loses = defaultdict(set)
    
    for w, l in results:
        wins[w].add(l)
        loses[l].add(w)

    for i in range(1, n + 1):
        for w in loses[i]:
            wins[w].update(wins[i])
        for ㅣ in wins[i]:
            loses[ㅣ].update(loses[i])
    
    return sum(1 for i in range(1, n + 1) if len(wins[i]) + len(loses[i]) == n - 1)
    