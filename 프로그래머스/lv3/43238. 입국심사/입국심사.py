def solution(n, times):
    answer = 0
    left, right = 0, max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        
        cnt = 0
        for t in times:
            cnt += mid // t
            if cnt >= n:
                break
                
        if cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer