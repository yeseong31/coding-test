from collections import Counter
from itertools import combinations


def solution(weights):
    answer = 0
    cnt = Counter(weights)
    target = [(3, 2), (4, 2), (4, 3)]

    for l, r in list(combinations(sorted(set(weights)), 2)):
        answer += sum(cnt[l] * cnt[r] for a, b in target if a * l == b * r)

    return answer + sum((c * (c - 1)) // 2 for c in cnt.values() if c > 1)