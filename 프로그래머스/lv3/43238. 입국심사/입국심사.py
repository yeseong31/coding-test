def binary_search(n, times):
    start, end = 1, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        check = 0
        for t in times:
            check += mid // t
            if check >= n:
                break
        if check >= n:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result

def solution(n, times):
    return binary_search(n, times)