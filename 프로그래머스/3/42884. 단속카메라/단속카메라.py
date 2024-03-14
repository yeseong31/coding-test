def solution(routes):
    answer = 0
    target = -30001
    
    for s, e in sorted(routes, key=lambda x: x[1]):
        if target < s:
            answer += 1
            target = e
    
    return answer
