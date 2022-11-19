def solution(stones, k):
    answer = 0
    left, right = 0, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        check = 0
        
        for stone in stones:
            if check == k:
                break
            if stone - mid <= 0:
                check += 1
            else:
                check = 0
                
        if check == k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer