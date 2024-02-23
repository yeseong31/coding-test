n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

answer = 0
left = 0
_sum = 0

for right in range(len(numbers)):
    _sum += numbers[right]

    while left <= right and _sum > k:
        answer += len(numbers) - right
        _sum -= numbers[left]
        left += 1

print(answer)
