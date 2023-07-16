def solution(stones, k):
    def available(n):
        jump = 0
        
        for stone in stones:
            # n명이 밟을 수 없다면 건너뛰기
            if stone - n < 0:
                jump += 1
                if jump >= k:
                    return False
            # 건너뛰어도 되지 않다면 건너뛴 횟수 초기화
            else:
                jump = 0
        
        return True
    
    
    answer = 0
    left, right = 0, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        # 현재 인원으로 징검다리를 건널 수 있는지 확인
        if available(mid):
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
        
    return answer