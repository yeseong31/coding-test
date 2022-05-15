# 풀이 2 - 스택 쌓기

# 변곡점을 기준으로 격차만큼 물 높이 volume을 채움
# 변곡점을 만날 때마다 스택에서 하나씩 꺼내면서 이전과의 차이만큼 물 높이를 채움

def trap(height: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우(높이 감소 -> 증가)
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            dist = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += dist * waters

        stack.append(i)

    return volume
