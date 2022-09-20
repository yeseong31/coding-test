def solution(stones, k):
    answer = 0
    left, right = 0, max(stones)

    while left <= right:
        mid = (left + right) // 2

        check = 0
        for s in stones:
            if check == k:
                break
            if s - mid <= 0:
                check += 1
            else:
                check = 0

        if check == k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
print(solution(stones, 3))
