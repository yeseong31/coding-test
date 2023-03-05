def solution(n, m, section):
    answer = 0
    while section:
        point = section.pop()
        while section and section[-1] > point - m:
            section.pop()
        answer += 1
        
    return answer