# 빗물 트래핑(180p)
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

def trap(height: list[int]) -> int:
    # 스택(구조물)
    stack = []
    # 물의 양
    volume = 0

    for i, h in enumerate(height):
        # height[stack[-1]]: 현재 기준 값(스택), height[i]: 현재 나의 위치
        while stack and height[stack[-1]] < height[i]:
            top = stack.pop()
            if not stack:
                break
            dist = i - stack[-1] - 1
            water_height = min(height[stack[-1]], height[i]) - height[top]
            volume += dist * water_height
        stack.append(i)

    return volume


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
# Output: 6

height = [4, 2, 0, 3, 2, 5]
print(trap(height))
