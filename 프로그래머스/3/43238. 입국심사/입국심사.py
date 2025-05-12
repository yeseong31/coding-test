def solution(n, times):
    times.sort()
    answer = times[-1] * n
    
    min_time = 0
    max_time = answer
    
    while min_time < max_time:
        current = (min_time + max_time) // 2
        
        required = 0
        for t in times:
            required += current // t
            if required >= n:
                break
        
        if required >= n:
            answer = min(answer, current)
            max_time = current
        else:
            min_time = current + 1
    
    return answer
