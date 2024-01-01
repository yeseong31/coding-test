def solution(n, cores):
    def check_cores(t):
        return sum(t // core for core in cores)

    if n < len(cores):
        return n

    n -= len(cores)
    left, right = 1, max(cores) * n
    target_time = right

    while left < right:
        mid = (left + right) // 2
        if check_cores(mid) >= n:
            right = mid
        else:
            left = mid + 1

    target_time = left
    remain_work = n - sum((target_time - 1) // core for core in cores)

    for i, core in enumerate(cores, 1):
        if target_time % core != 0:
            continue
        
        remain_work -= 1
        if remain_work == 0:
            return i
