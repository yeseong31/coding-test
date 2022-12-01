from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    for c in sorted(count, key=lambda x: count[x], reverse=True):
        k -= count[c]
        answer += 1
        if k <= 0:
            break
    
    return answer