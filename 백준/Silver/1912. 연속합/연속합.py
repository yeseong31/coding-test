n = int(input())
nums = list(map(int, input().split()))

answer = [nums[0]]
for i, v in enumerate(nums[1:]):
    answer.append(max(v + answer[i], v))
print(max(answer))