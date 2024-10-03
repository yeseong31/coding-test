def solution(diffs, times, limit):
    answer = int(10e15)
    
    time_prev = 0
    min_level, max_level = 1, max(diffs)
    
    while min_level <= max_level:
        level = (min_level + max_level) // 2
        
        spend_time = 0
        for diff, time_cur in zip(diffs, times):
            spend_time += time_cur
            if diff > level:
                spend_time += (time_prev + time_cur) * (diff - level)
                
            time_prev = time_cur
            
            if spend_time >= limit:
                break
            
        if spend_time <= limit:
            answer = min(answer, level)
            max_level = level - 1
        else:
            min_level = level + 1
        
    return answer
