def solution(n, m, section):
    answer = 0
    
    while section:
        answer += 1
        point = section.pop()
        
        while section and section[-1] > point - m:
            section.pop()
        
    return answer
