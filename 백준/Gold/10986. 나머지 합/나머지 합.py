n, m = map(int, input().split())
nums = list(map(int, input().split())) + [0]
count = [0] * m

for i in range(n):
    nums[i] += nums[i - 1]
    count[nums[i] % m] += 1

answer = count[0]
for c in count:
    answer += c * (c - 1) // 2
print(answer)