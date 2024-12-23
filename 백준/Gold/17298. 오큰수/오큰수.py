n = int(input())
nums = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n - 2, -1, -1):
    if nums[i] >= nums[i + 1]:
        while stack and nums[i] >= stack[-1]:
            stack.pop()
    else:
        stack.append(nums[i + 1])
    if stack:
        answer[i] = stack[-1]

print(*answer)