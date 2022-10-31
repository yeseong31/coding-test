def solution(a):
    if len(a) <= 3:
        return len(a)

    left, right = 0, len(a) - 1
    left_min, right_min = a[left], a[right]
    answer = 2

    while left < right:
        # 현재 값이 기존의 최솟값을 갱신시킨다면 +1
        target_left, target_right = a[left], a[right]
        if left_min > target_left:
            left_min = target_left
            answer += 1
        elif right_min > target_right:
            right_min = target_right
            answer += 1
        # 왼쪽 값이 오른쪽 값보다 크다면
        if a[left] > a[right]:
            left += 1
        else:
            right -= 1

    return answer


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
