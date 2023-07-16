def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    
    # distance에 위치한 돌 추가
    rocks.sort()
    rocks.append(distance)
    
    while start <= end:
        mid = (start + end) // 2
        prev = cnt = 0
        
        for rock in rocks:
            if rock - prev < mid:
                cnt += 1
            else:
                prev = rock
            if cnt > n:
                break
        
        if cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
        
    return answer