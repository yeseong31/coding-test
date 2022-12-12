_, _ = map(int, input().split())
walls = list(map(int, input().split()))

stack = []
answer = 0

for i, h in enumerate(walls):
    while stack and walls[stack[-1]] < h:
        b = walls[stack.pop()]
        if not stack:
            break
        d = i - stack[-1] - 1
        wh = min(walls[stack[-1]], h) - b
        answer += d * wh
    stack.append(i)

print(answer)