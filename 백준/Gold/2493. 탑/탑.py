# 송신탑의 수
n = int(input())
# 송신탑의 높이
height = list(map(int, input().split()))

stack = []
result = []
prev = 0
for i, h in enumerate(height):
    while stack and stack[-1][1] < h:
        stack.pop()
    if stack:
        result.append(stack[-1][0] + 1)
    else:
        result.append(0)
    stack.append((i, h))

print(*result)