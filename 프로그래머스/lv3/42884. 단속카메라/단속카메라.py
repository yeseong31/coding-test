def solution(routes):
    answer = 0
    target = -30001
    
    for start_time, end_time in sorted(routes, key=lambda x: x[1]):
        if target < start_time:
            answer += 1
            target = end_time
    
    return answer