# 풀이 1 - 투 포인터를 최대로 이동

# '최대 높이'는 전체 부피에 영향을 주지 않고 그저 왼쪽과 오른쪽을 나누는 장벽
# 최대 높이의 막대까지 각각 좌우 기둥 외채 높이 left_max, right_max가 현재 높이와의 차이만큼 물 높이를 더해 나감


def trap(height: list[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume
