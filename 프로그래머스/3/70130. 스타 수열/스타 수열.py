from collections import Counter


def solution(a):
    answer = -1
    counter = Counter(a)
    
    for k in counter:
        if counter[k] <= answer:
            continue
        
        cnt = 0
        i = 0
        
        while i < len(a) - 1:
            if a[i] == a[i + 1] or (a[i] != k and a[i + 1] != k):
                i += 1
            else:
                i += 2
                cnt += 1
    
        answer = max(answer, cnt)
    
    return -1 if answer < 0 else answer * 2