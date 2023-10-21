n, m, l = map(int, input().split())
s = [int(input()) for _ in range(m)] + [l]


def solution(q):
    left, right = 0, l
    result = 0

    while left <= right:
        mid = (left + right) // 2
        start = count = 0

        for cutting_point in s:
            if cutting_point - start >= mid:
                start = cutting_point
                count += 1

        if count > q:
            result = max(result, mid)
            left = mid + 1
        else:
            right = mid - 1

    return result


for _ in range(n):
    print(solution(int(input())))
