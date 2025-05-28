from collections import Counter


def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    
    for c in sorted(count, key=lambda x: count[x], reverse=True):
        answer += 1
        if (k := k - count[c]) <= 0:
            return answer
    
    return answer
