from collections import Counter

def solution(topping):
    answer = 0
    
    cnt = Counter(topping)
    chk = set()
    
    for t in topping:
        cnt[t] -= 1
        if cnt[t] == 0:
            cnt.pop(t)
        chk.add(t)
        if len(chk) == len(cnt):
            answer += 1
    
    return answer