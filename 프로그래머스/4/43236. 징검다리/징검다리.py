def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    
    answer = 0
    left = 0
    right = distance + 1
    
    while left < right:
        mid = (left + right) // 2
        
        prev = 0
        count = 0
        
        for _, r in enumerate(rocks):
            if r - prev < mid:
                count += 1
            else:
                prev = r
            
            if count > n:
                break
        
        if count > n:
            right = mid
        else:
            answer = mid
            left = mid + 1
    
    return answer
