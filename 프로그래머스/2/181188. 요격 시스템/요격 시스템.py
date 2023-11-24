def solution(targets):
    answer = 0
    targets.sort()
    
    while targets:
        start = targets.pop()[0]
        answer += 1
        
        while targets and start < targets[-1][1]:
            targets.pop()
        
    
    return answer
