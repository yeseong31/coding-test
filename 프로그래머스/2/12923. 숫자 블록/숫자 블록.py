def find(n):
    if n == 1:
        return 0

    result = 1
    
    for x in range(2, int(n ** 0.5) + 1):
        if n % x != 0:
            continue

        result = x
        if n // x <= 1e7:
            return n // x

    return result


def solution(begin, end):
    return [find(n) for n in range(begin, end + 1)]
