from collections import Counter


def solution(gems):
    answer = 0, len(gems)
    kind = set(gems)
    counter = Counter()
    
    l = 0
    for r in range(len(gems)):
        counter[gems[r]] += 1
        while len(counter) == len(kind):
            counter[gems[l]] -= 1
            if counter[gems[l]] == 0:
                del counter[gems[l]]
            l += 1            
            if r + 1 - l < answer[1] - answer[0]:
                answer = l, r + 1
    
    return answer