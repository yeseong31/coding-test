from collections import Counter
from itertools import combinations


def solution(weights):
    def check(x, y):
        for a, b in target:
            if a * x == b * y:
                return True
        return False

    answer = 0
    cnt = Counter(weights)
    target = [(3, 2), (4, 2), (4, 3)]

    for l, r in list(combinations(sorted(set(weights)), 2)):
        if check(l, r):
            answer += cnt[l] * cnt[r]
            
    return answer + sum((c * (c - 1)) // 2 for c in cnt.values() if c > 1)