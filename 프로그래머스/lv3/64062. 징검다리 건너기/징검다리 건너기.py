def solution(stones, k):
    answer = 0
    start, end = 0, max(stones)
    
    while start <= end:
        mid = (start + end) // 2
        result = True
        count = 0
        
        for stone in stones:
            if stone < mid:
                count += 1
                if count >= k:
                    result = False
            else:
                count = 0
        
        if result:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
        
    return answer