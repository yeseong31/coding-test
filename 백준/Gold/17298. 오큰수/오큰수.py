n = int(input())
nums = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i, v in enumerate(nums):
    while stack and stack[-1][0] < nums[i]:
        answer[stack.pop()[1]] = nums[i]
    
    stack.append((nums[i], i))
        
print(*answer)
