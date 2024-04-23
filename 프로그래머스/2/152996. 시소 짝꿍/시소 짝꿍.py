from collections import Counter
from itertools import combinations


def solution(weights):
    cnt = Counter(weights)
    answer = sum((c * (c - 1)) // 2 for c in cnt.values())
    target = [(3, 2), (4, 2), (4, 3)]

    for l, r in combinations(sorted(cnt), 2):
        answer += sum(cnt[l] * cnt[r] for a, b in target if a * l == b * r)
    return answer
