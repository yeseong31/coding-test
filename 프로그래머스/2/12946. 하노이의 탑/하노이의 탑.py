def hanoi(n, start, mid, end, result):
    if n == 1:
        result.append([start, end])
        return
    
    hanoi(n - 1, start, end, mid, result)
    hanoi(1, start, mid, end, result)
    hanoi(n - 1, mid, start, end, result)


def solution(n):
    result = []
    hanoi(n, 1, 2, 3, result)
    return result
