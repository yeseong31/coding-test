from collections import Counter


def solution(topping):
    answer = 0
    
    cnt = Counter(topping)
    check = set()
    
    for t in topping:
        cnt[t] -= 1
        if cnt[t] == 0:
            cnt.pop(t)
        
        check.add(t)
        if len(check) == len(cnt):
            answer += 1
    
    return answer
