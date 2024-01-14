def can_immigrate(n, times, mid):
    return sum(mid // time for time in times) >= n


def solution(n, times):
    left, right = 1, int(1e15)
    
    while left < right:
        mid = (left + right) // 2
        if can_immigrate(n, times, mid):
            right = mid
        else:
            left = mid + 1
    
    return left
