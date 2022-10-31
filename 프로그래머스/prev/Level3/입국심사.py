def solution(n, times):
    answer = 0
    l, r = 0, max(times) * n

    while l <= r:
        m = (l + r) // 2
        check = 0
        done = False

        for t in times:
            check += m // t
            if check >= n:
                done = True

        if done:
            answer = m
            r = m - 1
        else:
            l = m + 1

    return answer
