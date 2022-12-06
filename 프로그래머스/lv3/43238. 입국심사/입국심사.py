def solution(n, times):
    answer = 0
    l, r = 0, max(times) * n
    while l <= r:
        m = (l + r) // 2
        if sum([m // t for t in times]) >= n:
            answer = m
            r = m - 1
        else:
            l = m + 1
    return answer