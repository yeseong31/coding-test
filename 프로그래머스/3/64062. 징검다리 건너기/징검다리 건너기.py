def solution(stones, k):
    def check(n):
        jump = 0
        
        for stone in stones:
            if stone - n >= 0:
                jump = 0
            elif (jump := jump + 1) >= k:
                return False
        
        return True
    
    
    answer = 0
    left, right = 0, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        
        if check(mid):
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
        
    return answer