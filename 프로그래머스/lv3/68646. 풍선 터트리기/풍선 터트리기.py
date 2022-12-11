def solution(a):
    if len(a) <= 3:
        return len(a)
    
    l, r = 0, len(a) - 1
    left_min, right_min = a[l], a[r]
    answer = 2
    
    while l < r:
        cur_left, cur_right = a[l], a[r]
        if left_min > cur_left:
            left_min = cur_left
            answer += 1
        elif right_min > cur_right:
            right_min = cur_right
            answer += 1
        if a[l] > a[r]:
            l += 1
        else:
            r -= 1
    
    return answer


