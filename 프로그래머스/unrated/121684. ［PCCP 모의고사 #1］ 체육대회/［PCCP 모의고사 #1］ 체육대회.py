from itertools import permutations, combinations


def solution(ability):
    answer = -1
    n, m = len(ability), len(ability[0])
    
    for comb in combinations(range(n), m):
        for perm in permutations(range(m), m):
            answer = max(answer, sum(ability[c][p] for c, p in zip(comb, perm)))
    
    return answer