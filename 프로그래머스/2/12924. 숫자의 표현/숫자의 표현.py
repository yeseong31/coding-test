def solution(n):
    cnt = 0
    
    for i in range(n, 0, -1):
        target = n
        j = i
        
        while target > 0:
            target -= j
            j -= 1
            
            if j <= 0:
                break
        
        if target == 0:
            cnt += 1

    return cnt
